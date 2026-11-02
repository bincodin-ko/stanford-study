"""Combine every Markdown file of the study repo into one HTML book for PDF printing."""
import html
import os
import re
import subprocess
import sys

REPO = sys.argv[1]
OUT = sys.argv[2]

docs = sorted(f for f in os.listdir(f"{REPO}/docs") if re.match(r"\d\d-.*\.md$", f))
coding = sorted(f for f in os.listdir(f"{REPO}/docs/coding") if re.match(r"\d\d-.*\.md$", f))
files = (["README.md"] + [f"docs/{f}" for f in docs] + ["docs/coding/README.md"]
         + [f"docs/coding/{f}" for f in coding] + ["docs/sources.md"])

def prefix(rel):
    name = rel.replace("docs/coding/", "c-").replace("docs/", "d-").replace(".md", "").replace("README", "readme")
    return re.sub(r"[^a-z0-9-]", "-", name.lower()) + "--"

PREFIX = {os.path.normpath(f): prefix(f) for f in files}

def title_of(rel):
    for line in open(f"{REPO}/{rel}", encoding="utf-8"):
        if line.startswith("# "):
            return re.sub(r"[*`]", "", line[2:]).strip()
    return rel

def fix_links(body, rel):
    base = os.path.dirname(rel)

    def repl(m):
        href = m.group(1)
        if href.startswith(("http://", "https://", "mailto:", "#")):
            return m.group(0)
        path, _, anchor = href.partition("#")
        target = os.path.normpath(os.path.join(base, path))
        if target in PREFIX:
            new = "#" + PREFIX[target] + (anchor if anchor else "top")
            return f'href="{new}"'
        if target.endswith(".pptx"):
            return 'href="#readme--top"'
        return m.group(0)

    return re.sub(r'href="([^"]+)"', repl, body)

parts, toc = [], []
for rel in files:
    p = PREFIX[os.path.normpath(rel)]
    body = subprocess.run(
        ["pandoc", "-f", "gfm", "-t", "html5", f"--id-prefix={p}", f"{REPO}/{rel}"],
        capture_output=True, text=True, check=True).stdout
    body = fix_links(body, rel)
    body = body.replace("<details>", "<details open>")
    kind = "coding" if "coding/" in rel else ("intro" if rel == "README.md" else "biz")
    parts.append(f'<section class="chapter {kind}" id="{p}top">{body}</section>')
    toc.append((kind, p, title_of(rel)))

def toc_html():
    groups = {"intro": "시작하기", "biz": "인터넷 사업 공부 (1~82장)", "coding": "코딩 공부 노트"}
    out, last = [], None
    for kind, p, t in toc:
        if p == "d-sources--":
            kind = "src"
        if kind != last:
            if last:
                out.append("</ol>")
            out.append(f"<h3>{groups.get(kind, '참고 자료')}</h3><ol class='toc'>")
            last = kind
        out.append(f'<li><a href="#{p}top">{html.escape(t)}</a></li>')
    out.append("</ol>")
    return "\n".join(out)

CSS = open(os.path.join(os.path.dirname(__file__), "book.css"), encoding="utf-8").read()
doc = f"""<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>인터넷 사업 공부 교재</title>
<style>{CSS}</style></head><body>
<section class="cover">
  <div class="cover-kicker">1인 창업가 겸 개발자를 위한</div>
  <h1>인터넷 사업 공부 교재</h1>
  <p class="cover-sub">기획 · 만들기 · 출시 · 운영 · 마케팅 · 돈 벌기<br>+ 코딩 기초부터 고수까지</p>
  <p class="cover-meta">사업 1~82장 · 코딩 노트 13장 · 용어 사전 · 퀴즈 · 참고 자료<br>2026년 11월 기준</p>
  <p class="cover-note">법·세금·플랫폼 정책은 자주 바뀌어요. 실제로 적용하기 전에 각 장의 안내대로 공식 자료를 다시 확인하세요.</p>
</section>
<section class="toc-page"><h2>목차</h2><p class="toc-hint">제목을 누르면 해당 장으로 이동해요. 본문 속 "○장" 링크도 눌러서 이동할 수 있어요.</p>{toc_html()}</section>
{''.join(parts)}
</body></html>"""
open(OUT, "w", encoding="utf-8").write(doc)
print("files:", len(files), "html bytes:", len(doc))
