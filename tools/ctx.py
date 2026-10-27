#!/usr/bin/env python3
"""ctx.py - token-saving helpers for the resume workflow. Read-only on master files.

Run from the resumes folder (C:\\Users\\surface\\resumes):
  python3 tools/ctx.py sections <file-key|path> <sel> [<sel> ...]
        file keys: 01 02 03 04 05 SK (skills inventory) FC (fact-check)
        sel = section number or ID as it starts the heading: 6  6A  0A  2.1  PA-07  X-02
        A section includes its sub-sections. PA-07.3 is read as PA-07.
  python3 tools/ctx.py pack --ids PA-01,PA-07,X-02 --out <context_pack.md> [--label <text>]
  python3 tools/ctx.py verify <context_pack.md>
  python3 tools/ctx.py stats <resume.pdf> [<resume.pdf> ...]
"""
import argparse, datetime, hashlib, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER = os.path.join(ROOT, 'master', 'v2.0-draft')
FILES = {'01': '01_Resume_Master_Rules.md', '02': '02_Candidate_Profile.md',
         '03': '03_Achievement_Library.md', '04': '04_Resume_Layout_Spec.md',
         '05': '05_JD_Keyword_and_Matching_Rules.md',
         'SK': 'technical-skills-inventory.md', 'FC': 'fact-check-and-open-questions.md'}
# What every drafting context pack carries (verbatim). 03 achievement entries are added by --ids.
PACK_SPEC = [('01', ['2', '4', '6', '7', '9', '10']), ('02', ['1', '2', '6', '7', '8']),
             ('03', ['0', '0A']), ('04', ['3', '4', '5']), ('05', ['6', '7']),
             ('SK', [str(n) for n in range(1, 13)]), ('FC', ['0', '4'])]
HEAD = re.compile(r'^(#{1,6})\s+(.*)$')


def path_of(key):
    if key in FILES:
        return os.path.join(MASTER, FILES[key])
    for p in (key, os.path.join(ROOT, key), os.path.join(MASTER, key)):
        if os.path.exists(p):
            return p
    sys.exit('not found: ' + key)


def read(p):
    with open(p, encoding='utf-8') as fh:
        return fh.read()


def sha(p):
    with open(p, 'rb') as fh:
        return hashlib.sha1(fh.read()).hexdigest()[:12]


def version_line(text):
    for line in text.split('\n')[:12]:
        if line.startswith('**Version:**') or line.startswith('> 版本'):
            return line.split(' · **Status')[0].replace('**', '').strip()[:80]
    return '(no version line)'


def headings(lines):
    out, code = [], False
    for i, line in enumerate(lines):
        if line.startswith('```'):
            code = not code
            continue
        m = None if code else HEAD.match(line)
        if m:
            out.append((i, len(m.group(1)), m.group(2).strip()))
    return out


def token(title):
    parts = title.split()
    return parts[0].rstrip('.:·') if parts else ''


def norm(sel):
    m = re.match(r'^((?:PA|X)-\d+)\.\d+$', sel)
    return m.group(1) if m else sel


def extract(path, sels):
    lines = read(path).split('\n')
    hs = headings(lines)
    chunks, found = [], set()
    for k, (i, lvl, title) in enumerate(hs):
        for s in sels:
            if s in found:
                continue
            if token(title) == s or (' ' in s and title.startswith(s)):
                end = next((j for (j, l2, _) in hs[k + 1:] if l2 <= lvl), len(lines))
                chunks.append((s, '\n'.join(lines[i:end]).rstrip()))
                found.add(s)
    return chunks, [s for s in sels if s not in found]


def cmd_sections(a):
    p = path_of(a.file)
    sels = [norm(s) for s in a.sel]
    chunks, missing = extract(p, sels)
    print('<!-- %s | %s | sha1 %s -->' % (os.path.basename(p), version_line(read(p)), sha(p)))
    for s, body in chunks:
        print('\n<!-- § %s -->\n%s' % (s, body))
    if missing:
        print('\n<!-- NOT FOUND: %s -->' % ', '.join(missing))


def cmd_pack(a):
    ids = sorted({norm(x.strip()) for x in a.ids.split(',') if x.strip()},
                 key=lambda x: (x.split('-')[0], int(x.split('-')[1]) if '-' in x and x.split('-')[1].isdigit() else 0))
    spec = [(k, list(s)) for k, s in PACK_SPEC]
    spec[2][1].extend(ids)
    rows, body, missing_all, = [], [], []
    for key, sels in spec:
        p = path_of(key)
        chunks, missing = extract(p, sels)
        rows.append('| %s | %s | %s | %s | %s |' % (key, FILES[key], version_line(read(p)), sha(p), ' '.join(sels)))
        missing_all += ['%s §%s' % (key, m) for m in missing]
        for s, txt in chunks:
            body.append('\n---\n<!-- src: %s § %s -->\n%s' % (FILES[key], s, txt))
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    head = ['# Context Pack — %s' % (a.label or os.path.basename(os.path.dirname(os.path.abspath(a.out)))),
            '',
            '> Derived, read-only cache: verbatim excerpts of master\\v2.0-draft, generated %s by tools/ctx.py.' % now,
            '> Not a source of truth. Run `python3 tools/ctx.py verify <this file>`; if STALE, rebuild before use.',
            '',
            '| Key | File | Version | sha1 | Sections |', '|---|---|---|---|---|'] + rows + [
            '', 'IDs: ' + ', '.join(ids), 'Missing: ' + (', '.join(missing_all) or 'none')]
    text = '\n'.join(head + body) + '\n'
    with open(a.out, 'w', encoding='utf-8') as fh:
        fh.write(text)
    cjk = len(re.findall(r'[\u4e00-\u9fff]', text))
    print('pack written: %s | %.1f KB | ~%dK tokens | IDs %d | missing: %s'
          % (a.out, len(text.encode()) / 1024, (cjk + (len(text) - cjk) / 3.6) / 1000, len(ids), ', '.join(missing_all) or 'none'))


def cmd_verify(a):
    text = read(a.pack)
    stale = []
    for key, fname, ver, digest in re.findall(r'^\| (\w+) \| ([^|]+?) \| ([^|]+?) \| ([0-9a-f]{12}) \|', text, re.M):
        now = sha(os.path.join(MASTER, fname.strip()))
        if now != digest:
            stale.append('%s (%s → %s)' % (fname.strip(), digest, now))
    print('STALE: ' + '; '.join(stale) if stale else 'OK — pack matches current master files')
    sys.exit(1 if stale else 0)


BUL = re.compile(r'^\s*[•●▪·]\s')
SEC = re.compile(r'^\s*[A-Z][A-Z &,/\-–]{6,}\s*$')
IZE = re.compile(r'\b[a-z]{3,}iz(?:e|es|ed|ing|ation|ations)\b', re.I)
NOT_IZE = re.compile(r'^(size|sized|sizes|sizing|resize\w*|downsize\w*|prize|seize\w*)$', re.I)


def pdftext(pdf, first=None, last=None):
    cmd = ['pdftotext', '-layout'] + (['-f', str(first), '-l', str(last)] if first else []) + [pdf, '-']
    return subprocess.run(cmd, capture_output=True, text=True).stdout


def cmd_stats(a):
    for pdf in a.pdf:
        info = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout
        pages = int((re.search(r'Pages:\s+(\d+)', info) or [0, 0])[1])
        text = pdftext(pdf)
        lines = text.split('\n')
        width = max((len(l.rstrip()) for l in lines), default=1)
        bullets, cur, paras, run, widows = [], None, [], [], 0
        for l in lines + ['']:
            s = l.rstrip()
            if BUL.match(s):
                if cur: bullets.append(cur)
                cur = [s.strip()]
                if run: paras.append(run); run = []
                continue
            if cur and s.strip() and not SEC.match(s) and len(s) - len(s.lstrip()) >= 3 and not re.search(r'\s{4,}(19|20)\d\d', s):
                cur.append(s.strip()); continue
            if cur: bullets.append(cur); cur = None
            if s.strip() and not SEC.match(s) and len(s.strip()) > 0:
                run.append(s.strip())
                if len(s) < 0.8 * width:
                    if len(run) > 1 and len(s.strip()) <= 12: widows += 1
                    paras.append(run); run = []
            else:
                if run: paras.append(run); run = []
        n = len(bullets); by = {}
        for b in bullets: by[len(b)] = by.get(len(b), 0) + 1
        three = by.get(3, 0); over = [b[0][:60] for b in bullets if len(b) > 3]
        long_p = [p[0][:50] for p in paras if len(p) > 4 and len(' '.join(p)) > 300]
        p1 = pdftext(pdf, 1, 1)
        need = ['PROFESSIONAL SUMMARY', 'CORE COMPETENCIES', 'SELECTED ACHIEVEMENTS']
        miss1 = [x for x in need if x not in p1]
        banned = sorted(set(re.findall(r'\b(CEW|SCV-CCD|CCD|HCL)\b', text)))
        review = sorted(set(re.findall(r'\b(CTO|Chief Architect)\b', text)))
        ize = sorted({w.lower() for w in IZE.findall(text) if not NOT_IZE.match(w)})
        prog = len(re.findall(r'\bprograms?\b', text, re.I))
        verdict = []
        if pages > 3: verdict.append('pages>3')
        if over: verdict.append('bullets>3 lines')
        if n and three / n > 0.2: verdict.append('3-line bullets >20%')
        if long_p: verdict.append('paragraphs>4 lines')
        if miss1: verdict.append('page-1 composition')
        if banned: verdict.append('banned terms')
        if ize: verdict.append('-ize spelling')
        print('== %s' % os.path.basename(pdf))
        print('  pages %d | bullets %d by rendered lines %s | 3-line share %.0f%%' % (pages, n, dict(sorted(by.items())), 100 * three / n if n else 0))
        if over: print('  >3 lines: ' + ' | '.join(over))
        if long_p: print('  paragraphs >4 lines: ' + ' | '.join(long_p))
        print('  page 1 missing: %s | one-word last lines: %d' % (', '.join(miss1) or 'none', widows))
        print('  banned (01 §7): %s | review (title rule): %s | -ize: %s | "program(s)" x%d (allowed only in JD role title / software sense)'
              % (', '.join(banned) or 'none', ', '.join(review) or 'none', ', '.join(ize) or 'none', prog))
        print('  CHECK: ' + ('PASS' if not verdict else 'ATTENTION — ' + ', '.join(verdict)) + '  (approximate, from pdftotext layout)')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    s = sub.add_parser('sections'); s.add_argument('file'); s.add_argument('sel', nargs='+'); s.set_defaults(f=cmd_sections)
    p = sub.add_parser('pack'); p.add_argument('--ids', required=True); p.add_argument('--out', required=True); p.add_argument('--label'); p.set_defaults(f=cmd_pack)
    v = sub.add_parser('verify'); v.add_argument('pack'); v.set_defaults(f=cmd_verify)
    t = sub.add_parser('stats'); t.add_argument('pdf', nargs='+'); t.set_defaults(f=cmd_stats)
    a = ap.parse_args(); a.f(a)


if __name__ == '__main__':
    main()
