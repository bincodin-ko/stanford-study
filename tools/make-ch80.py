"""Rebuild docs/80-product-plan-han-bakwi.md from the product/ planning documents."""
import re
from datetime import date

PARTS = [
    ("product/docs/01-prd.md", "1부. 기획서 (PRD)"),
    ("product/docs/02-roadmap-steps.md", "2부. 진행표 — 단계와 스텝"),
    ("product/docs/03-architecture.md", "3부. 설계 — 구조·데이터·AI 코치·안정성"),
    ("product/docs/decisions/0001-web-service-with-ai-coach.md", "4부. 결정 기록 0001 — 웹 서비스 + AI 코치"),
    ("product/docs/decisions/0002-rust-axum-server-rendering.md", "5부. 결정 기록 0002 — Rust(Axum) + 서버 렌더링"),
]

out = [
    '# 80. 이 교재로 만드는 제품 — "한 바퀴" 기획 (실습 사례)', "",
    "> 지금까지 배운 내용을 **실제 제품 하나에 적용한 기획 문서**예요. 55장 실습 프로젝트의 실제 사례이자, 교재를 외우는 대신 **만들면서 단계별로 안내받는 웹 서비스**의 설계도예요.",
    f"> 원본 문서는 저장소의 `product/` 폴더에 있고, 이 장은 `tools/make-ch80.py`로 다시 만들어요. ({date.today().isoformat()} 기준)", "",
    "**이 장을 읽는 법**",
    "- 1부 기획서: 42장(검증)·62장(포지셔닝)·4장(MoSCoW)을 적용한 예",
    '- 2부 진행표: 1~81장을 **"순서대로 하는 일"**로 다시 묶은 것 — 교재 전체의 **실천용 목차**로도 쓸 수 있어요',
    "- 3부 설계: 58~60장(설계·DB·API)·65장(로그인)·67장(AI)·81장(최적화·안정화)을 적용한 예",
    "- 4~5부 결정 기록: 58장 ADR 양식으로 남긴 실제 결정", "", "---", "",
]
anchors = {
    "](02-roadmap-steps.md)": "](#2부-진행표--단계와-스텝)",
    "](01-prd.md)": "](#1부-기획서-prd)",
    "](03-architecture.md)": "](#3부-설계--구조데이터ai-코치안정성)",
}
for path, title in PARTS:
    text = open(path, encoding="utf-8").read()
    text = re.sub(r"^# .*\n", "", text, count=1)                       # drop the file's own H1
    lines, in_code = [], False
    for line in text.split("\n"):                                         # demote headings outside code
        if line.startswith("```"):
            in_code = not in_code
        if not in_code and re.match(r"^#{2,5} ", line):
            line = "#" + line
        lines.append(line)
    text = "\n".join(lines).replace("](../../docs/", "](").replace("](../../../docs/", "](")
    for a, b in anchors.items():
        text = text.replace(a, b)
    out += [f"## {title}", "", text.strip(), "", "---", ""]
out += [
    "### 이 장 요약",
    "1. 교재를 외우지 않고 **만들면서 그때그때 필요한 장을 안내받는** 웹 서비스 + AI 코치를 기획했다. 첫 사용자는 나, 첫 프로젝트는 이 제품 자체(도그푸딩).",
    "2. 진행표는 **0~7단계, 50개 스텝** — 각 스텝에 목표·체크리스트·완료 기준·관련 장·Claude 요청문이 있다. 출시 후 **안정화 기간**과 **측정 기반 최적화**까지 포함.",
    "3. 기술은 **Rust(Axum) + 서버 렌더링 + Supabase + 도커 호스팅**, 1주차부터 **테스트·CI·상태 확인·안전한 종료**를 넣고, AI 코치는 **서버에서만 호출하고 읽기·조언만** 한다.", "",
]
open("docs/80-product-plan-han-bakwi.md", "w", encoding="utf-8").write("\n".join(out))
print("chapter 80 rebuilt")
