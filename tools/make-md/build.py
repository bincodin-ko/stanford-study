"""교재 저장소의 모든 Markdown을 한 파일로 합쳐요 (다른 제품에 데이터로 넣기용).

사용법: python3 tools/make-md/build.py . export/인터넷-사업-공부-전체.md [진행표 YAML 경로]
- 파일마다 `<a id="문서-id"></a>` 기준점과 `<!-- source: 경로 -->` 주석을 붙여요.
- 다른 파일로 가는 링크(예: 30-x.md#절)는 합친 파일 안의 문서 기준점(#doc-…)으로 바꿔요.
"""
import datetime
import os
import re
import sys

REPO, OUT = sys.argv[1], sys.argv[2]
STEPS = sys.argv[3] if len(sys.argv) > 3 else None

def listdir(d):
    return sorted(f for f in os.listdir(f"{REPO}/{d}") if re.match(r"\d{2,4}-.*\.md$", f))

files = (["README.md"] + [f"docs/{f}" for f in listdir("docs")]
         + ["docs/coding/README.md"] + [f"docs/coding/{f}" for f in listdir("docs/coding")]
         + ["docs/sources.md", "product/README.md"]
         + [f"product/docs/{f}" for f in listdir("product/docs")]
         + [f"product/docs/decisions/{f}" for f in listdir("product/docs/decisions")])
files = [f for f in files if os.path.exists(f"{REPO}/{f}")]

def doc_id(rel):
    return "doc-" + re.sub(r"[^a-z0-9]+", "-", rel.lower().removesuffix(".md")).strip("-")

IDS = {os.path.normpath(f): doc_id(f) for f in files}

def title_of(rel):
    for line in open(f"{REPO}/{rel}", encoding="utf-8"):
        if line.startswith("# "):
            return re.sub(r"[*`]", "", line[2:]).strip()
    return rel

def fix_links(text, rel):
    base = os.path.dirname(rel)
    def repl(m):
        label, href = m.group(1), m.group(2)
        if href.startswith(("http://", "https://", "mailto:", "#")):
            return m.group(0)
        path = href.partition("#")[0]
        target = os.path.normpath(os.path.join(base, path))
        if target in IDS:
            return f"[{label}](#{IDS[target]})"
        return label  # PDF·슬라이드 등 합친 파일 밖의 것은 글자만 남김
    return re.sub(r"\[([^\]]*)\]\(([^)\s]+)\)", repl, text)

def section(rel):
    if rel == "README.md" or "/decisions/" in rel or rel.startswith("product/"):
        return "제품 기획" if rel.startswith("product/") else "시작하기"
    if "coding/" in rel:
        return "코딩 공부 노트"
    if rel == "docs/sources.md":
        return "참고 자료"
    return "인터넷 사업 공부"

out = [f"""---
title: 인터넷 사업 공부 — 전체 교재 (한 파일 데이터판)
source_repo: bincodin-ko/stanford-study
generated: {datetime.date.today().isoformat()}
documents: {len(files)}
language: ko
note: 법·세금·요금 정보는 조사 시점 기준이며 바뀔 수 있음. 각 장의 출처와 '확인하지 못한 것'은 참고 자료 문서에 있음.
---

# 인터넷 사업 공부 — 전체 교재 (한 파일 데이터판)

이 파일은 저장소의 모든 문서를 순서대로 합친 것이에요. 문서마다 `<!-- source: 경로 -->` 주석과 `<a id="doc-…">` 기준점이 있어 다시 나누거나(문서 단위 분할), 검색·임베딩 데이터로 쓰기 쉬워요.

## 목차
"""]
cur = None
for rel in files:
    sec = section(rel)
    if sec != cur:
        out.append(f"\n**{sec}**\n")
        cur = sec
    out.append(f"- [{title_of(rel)}](#{IDS[os.path.normpath(rel)]}) — `{rel}`")
if STEPS:
    out.append("\n**부록**\n\n- [진행표 데이터 (steps.yaml)](#doc-appendix-steps-yaml)")

for rel in files:
    body = open(f"{REPO}/{rel}", encoding="utf-8").read().rstrip()
    out.append(f"\n\n---\n\n<!-- source: {rel} | section: {section(rel)} -->\n<a id=\"{IDS[os.path.normpath(rel)]}\"></a>\n\n{fix_links(body, rel)}")

if STEPS:
    y = open(STEPS, encoding="utf-8").read().rstrip()
    out.append("\n\n---\n\n<!-- source: han-bakwi/content/roadmap/steps.yaml | section: 부록 -->\n"
               "<a id=\"doc-appendix-steps-yaml\"></a>\n\n# 부록. 진행표 데이터 (steps.yaml)\n\n"
               "제품(한바퀴 앱)이 읽는 0~7단계 스텝 데이터 원본이에요.\n\n```yaml\n" + y + "\n```")

open(OUT, "w", encoding="utf-8").write("\n".join(out) + "\n")
print(f"documents: {len(files)}  bytes: {os.path.getsize(OUT)}")
