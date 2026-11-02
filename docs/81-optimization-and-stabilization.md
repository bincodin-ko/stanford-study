# 81. 최적화와 안정화 — 빠르게, 그리고 멈추지 않게

> 속도 기초(코어 웹 바이탈)·오류 추적·비용은 [68장](68-performance-errors-costs.md), 모니터링·장애 대응은 [9장](09-operations.md), 배포·롤백은 [7장](07-deploy-and-update.md), 테스트는 [50장](50-testing-in-practice.md), DB 인덱스는 [59장](59-database-design.md)에 있어요. 이 장은 그 조각들을 **"최적화"와 "안정화"라는 두 일**로 묶어요.

| | 최적화 | 안정화 |
|---|---|---|
| 목표 | **더 빠르게, 더 싸게, 더 잘 팔리게** | **멈추지 않게, 멈춰도 빨리 회복하게** |
| 질문 | "어디가 느리고 비싼가?" | "어디가 깨지고, 깨지면 얼마나 퍼지나?" |
| 순서 | **안정화가 먼저** — 자주 멈추는 서비스를 빠르게 만들어도 소용없어요 | |

---

## 1부. 안정화

### 1. 출시 후 안정화 기간 (하이퍼케어)

**안정화 기간** = 출시 직후, **새 기능을 멈추고 버그·성능·문의 대응에만 집중**하는 기간이에요. 업계에서는 하이퍼케어(hypercare)라고도 불러요. 자료마다 **1~8주**로 다양하고, 날짜가 아니라 **"끝내는 기준"을 채우면** 끝내요.

| 할 것 | 내용 |
|---|---|
| **기능 동결** | 새 기능 배포 금지. 버그 수정·긴급 패치만 (승인된 것만) |
| **매일 점검** | 오류 추적(68장), 주문·가입 숫자, 문의 (9장 루틴을 하루 2번) |
| **빠른 대응 약속** | 1급 장애는 즉시, 2급은 당일 (9장 심각도) |
| **문제 목록** | 발견한 문제·고친 날짜·남은 것 |
| **끝내는 기준 (예)** | ① 1급 장애 7일 연속 0건 ② 오류율 목표 이하 ③ 같은 문의 반복 없음 ④ 미해결 버그 목록이 "다음에 해도 되는 것"만 남음 |

> 💡 1인 사업자라면: 출시일을 **휴가·큰 일정 직전으로 잡지 마세요.** 출시 후 2주는 **내가 대응할 수 있는 시간**이어야 해요(54장).

### 2. 가용성 목표(SLO)와 에러 예산 — "얼마나 멈춰도 되나"

구글 SRE(사이트 신뢰성 엔지니어링) 방식에서 나온 개념이에요.

| 용어 | 뜻 | 예 |
|---|---|---|
| **SLI** (지표) | 무엇으로 잴까 | "결제 요청 중 성공 비율", "페이지가 1초 안에 열린 비율" |
| **SLO** (목표) | 얼마를 목표로 | "한 달 동안 99.9% 성공" |
| **SLA** (약속) | 손님과 맺은 계약 | "99.5% 못 지키면 요금 10% 환불" (B2B, 12장) |
| **에러 예산** | 100% − 목표 = **실패해도 되는 양** | 99.9%면 한 달 약 43분 |

```python
MINUTES_PER_MONTH = 30 * 24 * 60          # 30일 기준 43,200분

for target in [99.0, 99.5, 99.9, 99.99]:
    budget = MINUTES_PER_MONTH * (100 - target) / 100
    print(f"목표 {target}% → 한 달에 멈춰도 되는 시간 약 {budget:,.1f}분 ({budget/60:.1f}시간)")

# 이번 달 장애 기록으로 남은 "에러 예산" 확인
outages = [12, 7, 20]                      # 분
used = sum(outages)
budget = MINUTES_PER_MONTH * 0.1 / 100     # 99.9% 목표
print(f"99.9% 목표: 예산 {budget:.1f}분 중 {used}분 사용 → 남은 예산 {budget - used:.1f}분")
print("→ 새 기능 배포 멈추고 안정화" if used > budget * 0.75 else "→ 계획대로 배포")
```

실행 결과 (직접 돌려 확인했어요):
```
목표 99.0% → 한 달에 멈춰도 되는 시간 약 432.0분 (7.2시간)
목표 99.5% → 한 달에 멈춰도 되는 시간 약 216.0분 (3.6시간)
목표 99.9% → 한 달에 멈춰도 되는 시간 약 43.2분 (0.7시간)
목표 99.99% → 한 달에 멈춰도 되는 시간 약 4.3분 (0.1시간)
99.9% 목표: 예산 43.2분 중 39분 사용 → 남은 예산 4.2분
→ 새 기능 배포 멈추고 안정화
```

- **에러 예산 규칙**: 예산이 많이 남으면 **새 기능을 빠르게**, 거의 다 썼으면 **기능을 멈추고 안정화**. "빨리 만들기 vs 안정적으로"의 싸움을 숫자로 정해요. (75%라는 기준은 예시예요 — 내가 정하면 돼요.)
- **1인 사업자에게 99.99%는 비현실적**이에요(한 달 4분). 처음엔 **99.5~99.9%**와, **결제·로그인처럼 중요한 기능만** 목표를 세우세요.
- 목표는 **손님이 느끼는 것**으로 재요. 서버가 살아 있어도 결제가 실패하면 실패예요(13장 "카드 결제만 실패" 사례).

### 3. 장애가 번지지 않게 — 타임아웃·재시도·차단기·대체 응답

외부 서비스(결제·택배 조회·AI·문자, 58장 감싸기)가 느려지거나 멈추면, 내 서비스까지 **줄줄이 멈출 수** 있어요. 막는 장치 4가지:

| 장치 | 뜻 | 없으면 |
|---|---|---|
| **타임아웃** | "3초 안에 답이 없으면 포기" | 응답 없는 요청이 쌓여 서버 전체가 멈춤 |
| **재시도 + 지수 백오프 + 지터** | 실패하면 기다렸다 다시. 기다림은 2배씩 늘리고(상한 있음), **무작위로 흩뜨림** | 모두가 동시에 다시 몰려와 더 크게 넘어짐 |
| **서킷 브레이커 (차단기)** | 연속 실패가 쌓이면 **잠시 아예 부르지 않음** | 고장 난 곳을 계속 두드려 회복도 늦어짐 |
| **기능 축소 운영 (대체 응답)** | 일부가 고장 나도 **핵심은 살림** | 택배 조회 하나 때문에 주문 페이지 전체가 안 열림 |

```python
import random, time

def call_with_retry(func, tries=4, base=0.1, cap=2.0):
    """실패하면 기다렸다가 다시. 기다리는 시간은 2배씩 + 무작위(지터), 최대 cap초."""
    for attempt in range(1, tries + 1):
        try:
            return func()
        except TimeoutError as e:
            if attempt == tries:
                raise
            wait = random.uniform(0, min(cap, base * 2 ** attempt))   # 지터: 0~상한 사이 무작위
            print(f"  {attempt}번째 실패({e}) → {wait:.2f}초 뒤 재시도")
            time.sleep(wait)

class CircuitBreaker:
    """연속 실패가 쌓이면 잠시 '차단' — 고장 난 곳을 계속 두드리지 않기."""
    def __init__(self, max_failures=3, cool_down=1.0):
        self.max_failures, self.cool_down = max_failures, cool_down
        self.failures, self.opened_at = 0, None

    def call(self, func, fallback):
        if self.opened_at and time.time() - self.opened_at < self.cool_down:
            return fallback()                                  # 차단 중: 바로 대체 응답
        try:
            result = func()
            self.failures, self.opened_at = 0, None            # 성공하면 원래대로
            return result
        except TimeoutError:
            self.failures += 1
            if self.failures >= self.max_failures:
                self.opened_at = time.time()                   # 차단 시작
            return fallback()

random.seed(1)
state = {"n": 0}
def flaky():                                   # 처음 두 번은 시간 초과, 세 번째에 성공
    state["n"] += 1
    if state["n"] < 3:
        raise TimeoutError("3초 안에 응답 없음")
    return "배송 조회 성공"
print("재시도:", call_with_retry(flaky))

def broken():                                  # 계속 고장 난 외부 서비스
    raise TimeoutError("응답 없음")
breaker = CircuitBreaker()
results = [breaker.call(broken, lambda: "잠시 후 다시 확인해 주세요") for _ in range(5)]
print("차단기:", results[-1], "| 실패 횟수", breaker.failures, "| 차단 중:", breaker.opened_at is not None)
```

실행 결과 (직접 돌려 확인했어요):
```
  1번째 실패(3초 안에 응답 없음) → 0.03초 뒤 재시도
  2번째 실패(3초 안에 응답 없음) → 0.34초 뒤 재시도
재시도: 배송 조회 성공
차단기: 잠시 후 다시 확인해 주세요 | 실패 횟수 3 | 차단 중: True
```

꼭 지킬 것 (아마존 빌더스 라이브러리 글의 원칙 포함):
- **재시도는 두 번 실행돼도 안전한 요청에만** — 결제처럼 부작용이 있는 요청은 **멱등성 키**가 있어야 재시도할 수 있어요(60장).
- **재시도는 한 곳에서만** — 화면·서버·라이브러리가 각자 3번씩 재시도하면 3×3×3 = 27배로 불어나요.
- 타임아웃 값은 **평소 응답 시간을 재 보고** 정해요. 검증된 라이브러리(HTTP 클라이언트)의 기능을 쓰세요.
- 위 코드는 원리 설명용이에요. 실제로는 **언어별 검증된 라이브러리**를 쓰세요. 아마존은 차단기 대신 비슷한 효과의 "토큰 버킷" 방식을 선호한다고 밝히기도 했어요 — 방식보다 **"고장 난 곳을 계속 두드리지 않는다"**는 원칙이 중요해요.

### 4. 배포를 안전하게 — 카나리·기능 스위치·롤백

| 방법 | 뜻 | 1인 사업자 버전 |
|---|---|---|
| **카나리 배포** | 새 버전을 **일부 손님(예: 5%)**에게 먼저 → 숫자를 보고 → 점점 늘림 (탄광의 카나리아처럼 먼저 위험을 알림) | 호스팅의 단계적 배포 기능, 또는 아래 기능 스위치로 |
| **기능 스위치 (피처 플래그)** | 코드는 배포하되 기능은 **설정으로 켜고 끔** | 설정 표에 `new_checkout = false` → 나만 켜 보기 → 전체 |
| **롤백** | 문제가 생기면 **이전 버전으로 즉시 되돌리기** (7장) | 되돌리는 방법을 **미리 연습** |
| **DB 변경 분리** | 칸 삭제·이름 변경은 코드 배포와 **따로, 나중에** (59장) | "추가 → 새 코드 → 옛 칸 삭제" 3단계 |

> 💡 **금요일 저녁 배포 금지**는 1인 사업자에게 특히 중요해요. 문제가 생기면 주말 내내 혼자 대응해야 해요.

### 5. 버티는 힘 확인 — 부하 테스트와 용량 계획

- **부하 테스트**(50장): 이벤트·광고·출시 전에 "동시에 몇 명까지 괜찮은가"를 스테이징에서 확인.
- **용량 계획** — 간단 버전:
```
평소 최대 동시 접속 × 행사 배수(광고·이벤트면 5~10배로 가정) = 대비할 접속 수
→ 부하 테스트로 버티는지 확인 → 안 되면: 캐시, 이미지 CDN, 서버 크기 올리기(36장), 대기열(선착순 행사)
```
- **천천히 쌓이는 한계**도 봐요: 디스크 용량, DB 크기, 무료 요금제 한도(36·68장). 80% 되면 알림.

---

## 2부. 최적화

### 6. 원칙: 재기 전에 고치지 마라

> "섣부른 최적화는 모든 악의 근원" — 컴퓨터 과학자 도널드 커누스의 유명한 말이에요.

- 느낌으로 "여기가 느릴 거야"라고 고치면 **엉뚱한 곳**을 고치는 경우가 대부분이에요.
- 순서: **① 숫자로 재기 → ② 가장 느린 곳 하나 찾기 → ③ 고치기 → ④ 다시 재기**
- 재는 도구: 페이지는 PageSpeed Insights(68장), 서버는 **요청별 응답 시간 로그**, 코드는 **프로파일러**(어느 함수가 시간을 쓰는지 보여 주는 도구 — 파이썬 `cProfile`, 러스트 `cargo flamegraph` 등), DB는 **쿼리 실행 계획**(`EXPLAIN`).

측정해서 고친 예 — 같은 조회를 인덱스 없이/있이:

```python
import sqlite3, time
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INTEGER, total INTEGER)")
db.executemany("INSERT INTO orders VALUES (?, ?, ?)", ((i, i % 5000, 10000) for i in range(300_000)))

def measure(label):
    start = time.perf_counter()
    for uid in range(200):                         # 200명의 주문 합계 조회
        db.execute("SELECT SUM(total) FROM orders WHERE user_id = ?", (uid,)).fetchone()
    ms = (time.perf_counter() - start) * 1000
    print(f"{label}: {ms:.0f}ms")
    return ms

before = measure("인덱스 없음")
db.execute("CREATE INDEX idx_orders_user ON orders(user_id)")
after = measure("인덱스 있음")
print(f"약 {before / after:.0f}배 빨라짐")
print(db.execute("EXPLAIN QUERY PLAN SELECT SUM(total) FROM orders WHERE user_id = 1").fetchall()[0][3])
```

이 작업 환경에서 실행한 결과 (컴퓨터마다 숫자는 달라요):
```
인덱스 없음: 1891ms
인덱스 있음: 4ms
약 454배 빨라짐
SEARCH orders USING INDEX idx_orders_user (user_id=?)
```
→ 마지막 줄의 **실행 계획**이 "인덱스를 써서 찾는다(SEARCH ... USING INDEX)"로 바뀐 걸 확인하는 게 핵심이에요. 인덱스가 없으면 "표 전체를 훑는다(SCAN)"로 나와요.

### 7. 가장 흔한 서버 성능 문제 — N+1 쿼리

목록을 보여 줄 때 **목록 1번 + 항목마다 1번씩** DB를 부르는 실수예요. AI가 만든 코드에서도 자주 나와요.

```python
import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE users  (id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INTEGER, total INTEGER);
""")
db.executemany("INSERT INTO users VALUES (?, ?)", [(i, f"손님{i}") for i in range(1, 101)])
db.executemany("INSERT INTO orders VALUES (?, ?, ?)", [(i, (i % 100) + 1, 10000) for i in range(1, 301)])

count = {"q": 0}
db.set_trace_callback(lambda sql: count.__setitem__("q", count["q"] + 1))   # 실행된 SQL 수 세기

# ✕ N+1: 회원 목록 1번 + 회원마다 주문 조회 100번
count["q"] = 0
for uid, name in db.execute("SELECT id, name FROM users").fetchall():
    db.execute("SELECT SUM(total) FROM orders WHERE user_id = ?", (uid,)).fetchone()
print("N+1 방식 쿼리 수:", count["q"])

# ○ 한 번에: JOIN + GROUP BY
count["q"] = 0
rows = db.execute("""
SELECT u.name, SUM(o.total) FROM users u
LEFT JOIN orders o ON o.user_id = u.id GROUP BY u.id
""").fetchall()
print("한 번에 가져오기 쿼리 수:", count["q"], "| 결과 행 수:", len(rows))
```

실행 결과 (직접 돌려 확인했어요):
```
N+1 방식 쿼리 수: 101
한 번에 가져오기 쿼리 수: 1 | 결과 행 수: 100
```
- 손님 100명일 땐 티가 안 나다가 **1만 명이 되면 갑자기 느려져요.** DB가 다른 서버에 있으면 쿼리마다 왕복 시간이 더해져 더 심해요.
- 해결: **JOIN**, **한 번에 묶어 조회**(`WHERE user_id IN (...)`), ORM을 쓴다면 **미리 함께 불러오기(eager loading)** 기능.
- > 💡 Claude에게: "이 화면을 그릴 때 DB 쿼리가 몇 번 실행되는지 세는 테스트를 만들어 줘. N+1이 있으면 고쳐 줘."

### 8. 최적화할 곳 지도 — 효과 큰 순서로

| 대상 | 흔한 방법 | 장 |
|---|---|---|
| **화면 속도** | 이미지 줄이기, 지연 로딩, 외부 스크립트 줄이기 | 68 |
| **DB** | 인덱스, N+1 제거, 필요한 칸만 조회, 목록은 페이지네이션 | 59·60 |
| **반복 계산** | 캐시 (바뀔 때 지우는 규칙도 같이) | 코딩 10 |
| **오래 걸리는 일** | 백그라운드 작업으로 분리 | 66 |
| **비용** | 클라우드 예산 알림, AI 작은 모델·캐시, 안 쓰는 구독 정리 | 67·68 |
| **전환율** | 상세 페이지·결제 단계 줄이기, A/B 테스트 | 11·48 |
| **광고** | 손익분기 ROAS, 소재 테스트 | 61 |

> **"전환율 1% → 2%"는 서버를 2배 빠르게 하는 것보다 매출에 훨씬 큰 영향**을 줄 때가 많아요. 기술 최적화만 최적화가 아니에요.

---

## 9. 정기 루틴에 넣기

| 주기 | 안정화 | 최적화 |
|---|---|---|
| **매일** | 오류 알림, 핵심 기능(결제·로그인) 성공률 | — |
| **매주** | 에러 예산 사용량, 장애 기록 | 가장 느린 페이지·API 3개 |
| **매월** | 롤백·복구 연습 (8장 복구 훈련과 함께) | 느린 쿼리 정리, 비용 점검(68장), 의존성 업데이트(79장) |
| **큰 행사 전** | 부하 테스트, 기능 동결 | 캐시·CDN 점검 |
| **출시 직후** | **안정화 기간** (1절) | 측정만, 큰 최적화는 안정화 후 |

---

### 이 장 요약
1. **안정화가 먼저**: 출시 후 **안정화 기간(기능 동결 + 끝내는 기준)**, **가용성 목표와 에러 예산**으로 "기능 vs 안정"을 숫자로 정한다.
2. 장애가 번지지 않게 **타임아웃·재시도(백오프+지터, 멱등한 요청만, 한 곳에서만)·차단기·대체 응답**, 배포는 **카나리·기능 스위치·롤백 연습**.
3. 최적화는 **재고 → 가장 느린 곳 하나 → 고치고 → 다시 재기**. 가장 흔한 범인은 **큰 이미지·인덱스 없음·N+1**, 매출에는 **전환율 최적화**가 더 클 때가 많다.

---

> 📚 이 장의 출처와 확인하지 못한 부분은 [참고 자료 모음](sources.md#8081장-제품-기획최적화와-안정화)에 있어요.
