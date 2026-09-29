# Week 1 — 코딩 LLM과 AI 개발 입문

> 목표: "Claude Code가 왜 이렇게 동작하지?"를 **모델 내부 원리**로 설명할 수 있게 되기.
> 이미 도구를 많이 써봤으니, 기초 사용법은 건너뛰고 **원리 ↔ 실무 경험 연결**에 집중한다.

## 읽는 순서 (경험자용 압축 버전)

| 순서 | 자료 | 번역본 경로 (`stanford-cs146s-kr/docs/week1/…`) | 권장 강도 |
|:-:|---|---|---|
| 1 | Deep Dive into LLMs (Karpathy, 3.5h) | `deep-dive-llms/kr/` | ⭐ 핵심 — 아래 챕터 위주 |
| 2 | Prompt Engineering Guide (DAIR.AI) | `prompt-engineering-guide/kr/` | 기법 6개만 정독 |
| 3 | How OpenAI Uses Codex (PDF) | `how-openai-uses-codex/kr/index.md` | 빠르게, 내 워크플로와 비교 |
| 4 | AI Prompt Engineering: A Deep Dive (Anthropic 팀 대담) | `ai-prompt-engineering-deep-dive/kr/` | 선택 — 관심 챕터만 |
| – | Prompt Engineering Overview (Google Cloud) | 웹사이트 | 건너뛰어도 됨 (입문용) |

### 1. Deep Dive into LLMs — 챕터 선택 가이드

전체 24챕터 중 **에이전트 실무와 직결되는 것**부터:

| 챕터 파일 | 한 줄 요지 | 실무 연결 포인트 |
|---|---|---|
| `tokenization.md`, `tokenization-spelling.md` | 모델은 글자가 아니라 토큰을 본다 | 글자 수 세기·철자·정확한 문자열 조작이 약한 이유 → 코드로 시키기 |
| `models-need-tokens-to-think.md` | 토큰 하나당 계산량은 고정 | "바로 답만 말해" 대신 추론을 먼저 쓰게 하면 정확도↑ / thinking 모델의 존재 이유 |
| `hallucinations-tool-use.md` | 모르는 걸 모른다고 말하도록 학습시키기 + 도구 사용 | 에이전트가 파일을 **읽고** 답하게 하는 게 기억에 의존하는 것보다 나은 이유 |
| `knowledge-of-self.md` | 모델의 "자기 인식"은 학습 데이터가 만든 것 | "너 어떤 모델이야?" 답을 믿으면 안 되는 이유 |
| `jagged-intelligence.md` | 스위스 치즈처럼 구멍 난 능력 | 어려운 건 잘하는데 쉬운 데서 틀림 → 항상 검증(테스트) 필요 |
| `pretraining-to-post-training.md`, `post-training-data.md` | SFT = 라벨러가 쓴 이상적 답변 모방 | 어시스턴트의 "성격"은 사후학습에서 온다 |
| `supervised-finetuning-to-rl.md`, `reinforcement-learning.md` | 검증 가능한 문제로 RL → 스스로 전략 발견 | 코딩/수학처럼 **정답 확인이 되는 영역**에서 모델이 특히 강한 이유 |
| `rlhf.md` | RLHF는 보상 모델을 속일 수 있어 오래 못 돌린다 | "RLHF는 진짜 RL이 아니다"라는 주장의 의미 |
| `deepseek-r1.md`, `alphago.md` | RL로 "생각하는 법"이 창발 | 추론 모델(thinking)과 일반 모델의 차이 |
| `grand-summary.md` | 전체 요약 | 마지막에 복습용 |

나머지(`pretraining-data`, `neural-network-*`, `inference`, `gpt2-*`, `llama-31-base-model`)는 시간이 되면 읽기. 내부 원리를 좋아하면 추천.

### 2. Prompt Engineering Guide — 정독할 6개 기법

에이전트가 내부적으로 이미 쓰고 있는 패턴들이다. 각 기법을 **Claude Code의 어떤 동작에 해당하는지** 매핑해 보자.

| 파일 | 기법 | 떠올릴 Claude Code 동작 (직접 채워보기) |
|---|---|---|
| `fewshot.md` | Few-shot | |
| `cot.md` | Chain-of-Thought | |
| `consistency.md` | Self-Consistency | |
| `prompt_chaining.md` | Prompt Chaining | |
| `react.md` | ReAct (Reason + Act) | |
| `reflexion.md` | Reflexion | |

(보너스: `rag.md`, `tot.md`, `meta-prompting.md`)

### 3. How OpenAI Uses Codex — 비교 포인트

내 Claude Code 사용 습관과 나란히 놓고 보기:

- Ask 모드 먼저 → Claude Code의 **plan mode**와 비교
- `AGENTS.md`로 지속 컨텍스트 → `CLAUDE.md`와 비교
- "GitHub 이슈처럼 프롬프트 쓰기" → 내가 평소 주는 지시와 뭐가 다른가
- Best-of-N → 병렬 세션/서브에이전트로 여러 해법 받아보기
- 작업 큐를 백로그로 → 백그라운드/클라우드 세션 활용

## 과제 (Fall 2026 버전) ⚠️ 번역 사이트와 다름

번역 사이트에는 예전 과제("LLM Prompting Playground")가 링크돼 있지만,
**현재 과제 레포(2026-09-23 업데이트)의 Week 1 과제는 새 버전이다:**

### "Trace Dissection of a Real Claude Code Session"

실제 Claude Code 세션을 **mitmproxy 리버스 프록시**로 가로채서, API 요청(`system`, `tools`, `messages`)을 해부하는 과제.
Claude Code를 많이 써본 사람에게 딱 맞다. "쓰기만 했던 도구의 속"을 보는 과제이기 때문.

| Part | 내용 | 배점 |
|---|---|:-:|
| I | 세션 캡처: 파일 2개 이상 수정 + 최소 1회 실패/복구 + 계획 수립 + 내 레포에서 | 15 |
| II | 시스템 프롬프트 주석: 구조, 톤/길이 제어, "하지 말 것" 조건, 환경 정보, `<system-reminder>` | 25 |
| III | 도구 설계 분석: 도구 개수 집계(내장/MCP/지연 로딩), 성격이 다른 도구 2개 인터페이스 분석 | 25 |
| IV | 행동 분석: 에러 복구, 계획, 작업 상태, 서브에이전트, 컨텍스트 관리 — 근거 인용 + `[OBSERVED]`/`[INFERRED]` 표시 | 25 |
| V | 회고: 따라 할 설계 2개, 다르게 할 설계 1개, 내 사용 습관에서 바뀔 점 1개 | 10 |

핵심 세팅 (로컬 머신에서):

```bash
pip install mitmproxy   # 또는 brew install --cask mitmproxy
mitmweb --listen-host 127.0.0.1 --listen-port 58888 \
        --web-open-browser --mode reverse:https://api.anthropic.com \
        -w session.flows      # git 레포 밖에서 실행!
```

실험용 레포의 `.claude/settings.json`에 **프로젝트 단위로만** 추가해야 한다(`~/.claude`에 넣지 말 것):

```json
{ "env": { "ANTHROPIC_BASE_URL": "http://127.0.0.1:58888", "ENABLE_TOOL_SEARCH": "true" } }
```

주의:
- 캡처에는 API 키, 소스코드, `.env` 내용이 들어 있을 수 있다. `session.flows`는 절대 커밋하지 말고, 인용할 때는 `[REDACTED: ...]`로 가리기.
- 과제가 끝나면 `ANTHROPIC_BASE_URL` 설정을 지우기.
- 원문: https://github.com/mihail911/modern-software-dev-assignments/blob/master/week1/assignment.md

> 💡 과제를 하기 전에 읽을거리 1~2를 먼저 보면 좋다. Part II/III에서 "이 문장은 어떤 실패를 막으려고 들어갔나?"를 답할 때
> 환각·토큰·들쭉날쭉한 지능 같은 개념이 그대로 쓰인다.

## 체크 질문 (읽고 나서 답해보기)

1. LLM이 "strawberry에 r이 몇 개?" 같은 질문에서 틀리기 쉬운 이유를 **토큰화** 관점에서 설명하고, 에이전트라면 어떻게 우회하는지 말해보라.
2. "토큰 하나당 계산량이 고정"이라는 사실이 (a) CoT 프롬프팅, (b) thinking 모델, (c) "설명 없이 답만 줘" 지시에 각각 무엇을 의미하나?
3. SFT로 만든 어시스턴트와 RL로 훈련한 추론 모델은 "무엇을 모방하느냐"에서 어떻게 다른가? Karpathy의 "라벨러 시뮬레이션" 비유를 써서.
4. RLHF를 오래 돌리면 왜 문제가 생기나? 코딩처럼 검증 가능한 영역의 RL과 무엇이 다른가?
5. 환각을 줄이는 두 가지 방법(학습 쪽, 사용 쪽)은? Claude Code가 답하기 전에 파일을 `Read`하는 것과 어떻게 연결되나?
6. ReAct와 Reflexion은 각각 Claude Code 세션의 어떤 장면에 해당하나?
7. Codex 문서의 모범 사례 중 내가 **이미 하고 있는 것 하나**, **안 하고 있는데 도입할 것 하나**를 골라라.

## 내 노트

<!-- 읽으면서 떠오른 것, 질문, 체크 질문 답을 여기에 -->
