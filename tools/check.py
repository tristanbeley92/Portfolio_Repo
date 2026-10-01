"""Validate generated HTML, exact-case local links, and asset budgets."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
ROOT = Path(__file__).resolve().parent.parent
class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids, self.links, self.h1 = [], [], 0
        self.feed(path.read_text(encoding='utf-8'))
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs: self.ids.append(attrs['id'])
        if tag == 'h1': self.h1 += 1
        for key in ('href', 'src'):
            if key in attrs: self.links.append(attrs[key])
pages = {p.name: Page(p) for p in ROOT.glob('*.html')}
files = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts}
for name, page in pages.items():
    assert page.h1 == 1, f'{name}: expected one h1'
    assert len(page.ids) == len(set(page.ids)), f'{name}: duplicate IDs'
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc: continue
        target = unquote(url.path) or name
        assert target in files, f'{name}: missing local target {target}'
        if url.fragment and target in pages:
            assert url.fragment in pages[target].ids, f'{name}: missing fragment {link}'
assert (ROOT / 'script.js').stat().st_size < 10000
assert (ROOT / 'assets/hockey.webp').stat().st_size < 200000
print(f'PASS: {len(pages)} pages, local links and fragments, unique IDs, and asset budgets.')
print('JavaScript bytes:', (ROOT / 'script.js').stat().st_size)
print('Hockey image bytes:', (ROOT / 'assets/hockey.webp').stat().st_size)
