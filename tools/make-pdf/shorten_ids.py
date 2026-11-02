"""Replace long (Korean) heading ids with short ones so PDF named destinations stay small."""
import re
import sys
import urllib.parse

src, out = sys.argv[1], sys.argv[2]
s = open(src, encoding="utf-8").read()
seen = {}
for i in re.findall(r'id="([^"]+)"', s):
    seen.setdefault(i, f"x{len(seen)}")
s = re.sub(r'id="([^"]+)"', lambda m: f'id="{seen[m.group(1)]}"', s)
s = re.sub(r'href="#([^"]+)"',
           lambda m: f'href="#{seen.get(m.group(1), seen.get(urllib.parse.unquote(m.group(1))))}"', s)
if 'href="#None"' in s:
    sys.exit("some internal links point to missing headings")
open(out, "w", encoding="utf-8").write(s)
print("ids:", len(seen))
