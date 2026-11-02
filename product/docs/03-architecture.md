# 03. 설계 — 구조·데이터·AI 코치·보안

> 이 문서는 교재 [58장(설계)](../../docs/58-architecture-and-modules.md)·[59장(DB)](../../docs/59-database-design.md)·[60장(API)](../../docs/60-api-design.md)·[65장(로그인)](../../docs/65-auth-and-accounts.md)·[67장(AI 기능)](../../docs/67-adding-ai-features.md)을 이 제품에 적용한 결과예요.

---

## 1. 기술 선택 (제안 — 승인 필요)

| 부분 | 선택 | 이유 |
|---|---|---|
| 화면 + 서버 | **Next.js (TypeScript)** | 화면과 서버 코드를 한 프로젝트에서, AI 도구가 가장 잘 아는 조합 중 하나 |
| 로그인 + DB | **Supabase** (Auth + Postgres + RLS) | 로그인을 직접 안 만들어도 됨(65장), 무료로 시작, RLS로 내 데이터 보호(59장) |
| 배포 | **Vercel** | Next.js 배포가 가장 쉬움, 무료로 시작 (36장) |
| AI 코치 | **Claude API** (서버에서만 호출) | 모델은 만들 때 최신 공식 문서로 고르기 (67장) |
| 교재 콘텐츠 | 이 저장소의 `docs/*.md` | 앱 빌드 때 함께 넣어 앱 안에서 렌더링 |
| 진행표 콘텐츠 | `content/roadmap/*.yaml` | 스텝 데이터 (02 문서의 예시 형식) |
| 결제 (나중에) | 토스페이먼츠 등 국내 PG | 39장 |

비용: 나만 쓰는 단계는 **AI API 사용료 외에는 거의 0원**이 목표예요(무료 요금제 범위).

## 2. 폴더 구조 (58장 — 기능별)

```
han-bakwi/
├── CLAUDE.md                 ← 구조 규칙 (아래 6절)
├── content/
│   ├── roadmap/              ← 0~7단계 스텝 YAML
│   └── docs/                 ← 교재 마크다운 (stanford-study에서 복사)
├── src/
│   ├── app/                  ← 화면·주소 (Next.js)
│   ├── features/
│   │   ├── projects/         ← 프로젝트 만들기·정보
│   │   ├── roadmap/          ← 진행표·스텝·체크 상태
│   │   ├── docs/             ← 장 읽기
│   │   └── coach/            ← AI 코치 (프롬프트 조립, 사용 한도)
│   ├── lib/
│   │   ├── ai/               ← Claude API 호출은 여기서만
│   │   └── supabase/         ← DB 연결
│   └── shared/               ← 진짜 공통인 것만
├── supabase/migrations/      ← DB 변경 기록 (59장)
└── docs/decisions/           ← ADR
```

## 3. 데이터 설계 (59장)

```
auth.users (Supabase 기본)
   1
   │
   ▼ 다
projects ──1──< step_progress          (스텝마다 체크·메모·산출물)
   │
   └──1──< coach_messages              (AI 코치 대화 + 토큰 수)
```

| 표 | 칸 | 메모 |
|---|---|---|
| **projects** | id, user_id, name, idea, target_customer, weekly_hours, current_step_id, created_at | user_id에 인덱스 |
| **step_progress** | project_id, step_id, status(todo/doing/done/skipped), checklist(jsonb), notes, artifact(jsonb), updated_at | PK (project_id, step_id) |
| **coach_messages** | id, project_id, step_id, role(user/assistant), content, tokens_in, tokens_out, created_at | 비용 집계용 토큰 기록 |
| **usage_daily** | user_id, date, ai_calls, tokens_in, tokens_out | 하루 사용 한도 확인 |

- 스텝 정의 자체는 DB가 아니라 **파일(YAML)**에 둬요 → Git으로 버전 관리, 고치기 쉬움.
- **모든 표에 RLS**: "자기 프로젝트만" (59장 예시 정책).
- 시각은 `timestamptz`, 삭제 대신 상태값.

## 4. 화면 (48장 — 첫 화면에 할 일 하나)

| 화면 | 주인공 행동 |
|---|---|
| 첫 방문 / 소개 | "내 프로젝트 시작하기" |
| 프로젝트 만들기 (질문 4개) | 아이디어·손님·주당 시간·만드는 방식(빌더/직접) |
| **진행표 (홈)** | **"지금 할 스텝 열기"** — 0~7단계, 현재 위치 강조 |
| 스텝 화면 | 체크리스트 → 요청문 복사 → 산출물 저장 → "완료" |
| 장 읽기 | 스텝에서 바로 해당 소제목으로 이동 |
| AI 코치 (옆 패널) | "막혔어요" / "다음 뭐 해요?" / 자유 질문 |

## 5. AI 코치 설계 (67장)

```
[손님 질문]
   ▼
[서버: coach 모듈]
 ① 로그인·하루 한도 확인 (usage_daily)
 ② 맥락 조립:
    - 시스템 지시: 역할, 말투(쉬운 한국어), 규칙(법·세금은 "공식 확인 필요")
    - 내 프로젝트 정보 (아이디어·손님·현재 스텝)
    - 현재 스텝 정의 (목표·체크·완료 기준)
    - 관련 장 본문 (스텝에 연결된 장의 해당 절만 — 처음엔 검색 없이)
    - 최근 대화 몇 개
 ③ Claude API 호출 (lib/ai, 출력 길이 제한)
 ④ 토큰 기록 → 답 + "근거: ○장 ○절" 링크
```
- **처음엔 RAG 검색 없이** "스텝 → 연결된 장"으로 넣어요. 장이 정해져 있어서 충분하고 단순해요. 나중에 자유 질문이 많아지면 검색 추가.
- **프롬프트 인젝션 대비**: 코치는 **읽기·조언만**, DB 수정·스텝 완료 처리는 손님이 버튼으로 (AI에게 권한 없음).
- **비용**: 나만 쓰는 단계는 하루 50회 한도로 시작, 화면에 이번 달 사용량 표시.

## 6. CLAUDE.md에 넣을 규칙 (초안)

```markdown
# 한 바퀴 — 프로젝트 규칙
- 사용자는 초보자. 화면 문구는 쉬운 한국어, 전문 용어는 처음 나올 때 풀이
- 기능별 폴더(src/features/*). 화면 → features → lib 방향으로만 호출
- Claude API 호출은 src/lib/ai 에서만. 키는 환경 변수, 클라이언트 코드에 절대 넣지 않기
- Supabase 표를 만들면 RLS + "본인 데이터만" 정책을 같은 마이그레이션에
- 법·세금·숫자 안내 문구에는 반드시 "공식 확인 필요" 표시
- 작업 순서: 탐색 → 계획(내가 승인) → 구현 → 테스트 → 커밋
```

## 7. 보안 체크 (37·65·67장에서 이 제품에 해당하는 것)

| 항목 | 이 제품에서 |
|---|---|
| 비밀 키 | Supabase 서비스 키·Claude 키는 서버 환경 변수만 |
| 권한 | RLS + 서버에서 project.user_id 확인 |
| AI 남용 | 로그인 필수 + 하루 한도 + 분당 제한 |
| 개인정보 | 수집: 이메일만 (+ 프로젝트 메모). AI 회사로 전송됨을 처리방침에 명시 |
| 관리자 | Supabase 대시보드 2단계 인증 |

## 8. 결정이 필요한 것 (ADR 후보)

| # | 결정 | 제안 |
|---|---|---|
| 0001 | 웹 서비스 + AI 코치로 시작 | ✅ 사용자 결정 (2026-11-02) |
| 0002 | Next.js + Supabase + Vercel | 제안 — 승인 필요 |
| 0003 | 앱은 **새 깃허브 저장소**에서 개발, 교재는 이 저장소에서 복사 | 제안 — 승인 필요 |
| 0004 | 처음엔 검색(RAG) 없이 스텝-장 연결로 맥락 구성 | 제안 |
