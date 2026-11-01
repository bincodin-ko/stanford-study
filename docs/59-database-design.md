# 59. 데이터베이스 설계 — 표를 어떻게 나눌까

> 데이터베이스와 SQL 기초는 [코딩 9장](coding/09-web-development.md), 백업은 [8장](08-backup-and-recovery.md), 접근 규칙(RLS)은 [37장](37-security-must-dos.md)과 [57장](57-vibe-coding-money-cases.md)의 실패 사례를 함께 보세요.

**데이터베이스(DB) 설계** = 회원·상품·주문 같은 정보를 **어떤 표(테이블)에, 어떤 칸(컬럼)으로, 어떻게 연결해** 담을지 정하는 일이에요.

코드는 나중에 고치기 쉽지만, **데이터 구조는 한번 손님 데이터가 쌓이면 바꾸기 어려워요.** 그래서 처음에 조금 신경 쓸 가치가 있어요.

---

## 1. 기본 용어

| 용어 | 엑셀로 치면 | 뜻 |
|---|---|---|
| **테이블** | 시트 하나 | 한 종류의 정보 묶음 (회원, 상품, 주문) |
| **행(row)** | 한 줄 | 하나의 회원, 하나의 주문 |
| **컬럼(column)** | 한 칸의 제목 | 이메일, 가격, 주문일 |
| ★ **기본 키 (PK)** | 줄 번호 | 각 행을 하나로 구분하는 값. 보통 `id` |
| ★ **외래 키 (FK)** | 다른 시트의 줄 번호 | 다른 테이블의 행을 가리키는 칸 (주문의 `user_id` → 회원) |
| **인덱스** | 책 뒤의 찾아보기 | 자주 찾는 칸을 빨리 찾게 해 주는 목록 |
| **제약 조건** | 입력 규칙 | "비워 두면 안 됨", "중복 안 됨", "0 이상" 같은 규칙 |

---

## 2. 설계 순서 — 5단계

```
① 명사 찾기 → ② 관계 정하기 → ③ 칸 정하기 → ④ 규칙 붙이기 → ⑤ 자주 쓸 조회 확인
```

### ① 명사 찾기
서비스 설명을 쓰고 **명사**에 밑줄을 그어요.
> "**회원**이 **상품**을 골라 **주문**하고, 주문에는 여러 상품이 **수량**과 함께 담긴다."

→ 후보: 회원(users), 상품(products), 주문(orders), 주문 항목(order_items)

### ② 관계 정하기
| 관계 | 예 | 표현 방법 |
|---|---|---|
| **1 : 다** | 회원 1명 → 주문 여러 개 | 주문 표에 `user_id` (외래 키) |
| **다 : 다** | 주문 하나에 상품 여러 개, 상품 하나는 여러 주문에 | **중간 표**(`order_items`)를 만들어 연결 |
| **1 : 1** | 회원 ↔ 회원 상세 정보 | 대부분 그냥 한 표에 합쳐도 됨 |

```
users 1 ──< orders 1 ──< order_items >── 1 products
(회원)      (주문)        (주문 항목)        (상품)
```

### ③ 칸 정하기 — 한 칸에 한 값
- ✕ `상품목록: "그래놀라 2개, 요거트 1개"` (한 칸에 여러 값 → 검색·합계 불가)
- ○ `order_items` 표에 한 줄씩

### ④ 규칙 붙이기
- 꼭 있어야 하는 칸: `NOT NULL`
- 중복되면 안 되는 칸: `UNIQUE` (이메일)
- 값 범위: `CHECK (price >= 0)`
- 연결: `REFERENCES` (외래 키) → **없는 회원의 주문**이 생기지 않게

### ⑤ 자주 쓸 조회 확인
"내 주문 목록", "이번 달 매출" 같은 조회를 미리 적어 보고, 그 조회에 쓰는 칸에 **인덱스**를 붙여요.

---

## 3. 실습 — 작은 쇼핑몰 표 만들기

파이썬에 기본으로 들어 있는 SQLite로 바로 돌려 볼 수 있어요.

```python
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("PRAGMA foreign_keys = ON")
db.executescript("""
CREATE TABLE users (
  id         INTEGER PRIMARY KEY,
  email      TEXT NOT NULL UNIQUE,
  name       TEXT NOT NULL,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE products (
  id    INTEGER PRIMARY KEY,
  name  TEXT NOT NULL,
  price INTEGER NOT NULL CHECK (price >= 0)   -- 원 단위 정수
);
CREATE TABLE orders (
  id         INTEGER PRIMARY KEY,
  user_id    INTEGER NOT NULL REFERENCES users(id),
  status     TEXT NOT NULL DEFAULT 'paid',
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE order_items (
  order_id   INTEGER NOT NULL REFERENCES orders(id),
  product_id INTEGER NOT NULL REFERENCES products(id),
  qty        INTEGER NOT NULL CHECK (qty > 0),
  unit_price INTEGER NOT NULL,      -- 주문 당시 가격을 따로 저장
  PRIMARY KEY (order_id, product_id)
);
CREATE INDEX idx_orders_user ON orders(user_id);
""")
db.execute("INSERT INTO users (id, email, name) VALUES (1, 'kim@example.com', '김손님')")
db.executemany("INSERT INTO products VALUES (?, ?, ?)", [(1, '그래놀라', 12900), (2, '요거트', 3000)])
db.execute("INSERT INTO orders (id, user_id) VALUES (100, 1)")
db.executemany("INSERT INTO order_items VALUES (100, ?, ?, ?)", [(1, 2, 12900), (2, 1, 3000)])
db.execute("UPDATE products SET price = 13900 WHERE id = 1")   # 나중에 가격 인상
row = db.execute("""
SELECT u.name, o.id, SUM(oi.qty * oi.unit_price) AS total
FROM orders o
JOIN users u        ON u.id = o.user_id
JOIN order_items oi ON oi.order_id = o.id
GROUP BY o.id
""").fetchone()
print(row)
try:
    db.execute("INSERT INTO orders (id, user_id) VALUES (101, 999)")
except sqlite3.IntegrityError as e:
    print("막힘:", e)
print(0.1 + 0.2)
```

실행 결과 (직접 돌려 확인했어요):
```
('김손님', 100, 28800)
막힘: FOREIGN KEY constraint failed
0.30000000000000004
```

여기서 배울 점 세 가지:
1. **가격을 올려도 지난 주문 금액은 그대로**(28,800원)예요. `order_items`에 **주문 당시 가격**(`unit_price`)을 따로 저장했기 때문이에요. 상품 표의 가격만 보고 계산하면 과거 매출이 바뀌어 버려요.
2. **없는 회원(999번)의 주문은 DB가 막아요.** 외래 키 덕분이에요. (SQLite는 `PRAGMA foreign_keys = ON`을 켜야 검사해요.)
3. `0.1 + 0.2`가 정확히 `0.3`이 아니에요. 그래서 **돈은 소수(실수형)로 저장하면 안 돼요.** 아래 4절을 보세요.

---

## 4. 초보자가 자주 하는 실수와 규칙

| 실수 | 왜 문제인가 | 이렇게 |
|---|---|---|
| **돈을 실수형(float)으로** | 계산 오차 (0.1+0.2≠0.3) | 원화는 **원 단위 정수**. 달러처럼 소수가 있으면 **센트 단위 정수**나 `numeric` 타입 + 통화 칸 |
| **주문에 상품 가격을 저장 안 함** | 가격 바꾸면 과거 매출이 바뀜 | 주문 항목에 **당시 가격** 저장 |
| **한 칸에 여러 값** | 검색·합계 불가 | 표를 나눠 한 줄씩 |
| **같은 정보를 여러 표에 복사** | 한쪽만 고치면 서로 달라짐 | 한 곳에 두고 **외래 키로 연결** (정규화) |
| **시간대 없는 시각** | 서버 위치·서머타임에 따라 꼬임 | PostgreSQL은 `timestamptz`, 저장은 **UTC**, 화면에서 한국 시간으로 |
| **진짜 삭제** | 주문·정산 기록이 사라짐 | 주문·결제는 지우지 말고 `status`를 `canceled`로. 개인정보는 법에 따라 파기 (10장) |
| **비밀번호를 그대로 저장** | 유출 시 대형 사고 | 직접 만들지 말고 **인증 서비스·검증된 라이브러리**가 해시로 저장 (37장) |
| **DB를 손으로 직접 수정** | 무엇을 바꿨는지 기록 없음 | **마이그레이션 파일**로 변경 (6절) |

### 정규화 — "같은 정보는 한 곳에만"
- **정규화** = 중복을 없애도록 표를 나누는 규칙이에요. 교과서에는 1·2·3 정규형이 나와요.
  - **1정규형**: 한 칸에 한 값, 각 줄을 구분하는 키가 있음
  - **2정규형**: 모든 칸이 **키 전체**에 대한 정보
  - **3정규형**: 키가 아닌 칸을 통해 정해지는 정보는 따로 뺌 (예: 주문 표에 회원 주소를 복사해 두지 않기)
- 실무에서는 **"같은 사실을 두 군데 적지 않는다"**만 기억해도 충분해요.
- 예외: 주문 당시 가격·배송지처럼 **"그때의 기록"**이 필요한 값은 일부러 복사해 둬요. 복사가 아니라 **기록**이에요.

---

## 5. 인덱스 — 빨라지지만 공짜는 아님

- 인덱스가 없으면 DB가 **표 전체를 처음부터 끝까지** 훑어요. 손님이 많아지면 느려져요.
- 인덱스를 붙일 곳:
  - 외래 키 칸 (`orders.user_id`)
  - 자주 검색·정렬하는 칸 (`orders.created_at`, `users.email`)
  - RLS 정책에서 비교하는 칸 (수파베이스 공식 문서 권장)
- 단점: 저장할 때마다 인덱스도 갱신해야 해서 **쓰기가 조금 느려지고 용량**이 늘어요. 모든 칸에 붙이지 않아요.

---

## 6. 마이그레이션 — DB 구조 바꾸기를 기록하기

**마이그레이션** = "표에 칸 추가", "새 표 만들기" 같은 변경을 **번호 붙은 파일**로 남기는 방법이에요.

```
migrations/
├── 0001_create_users.sql
├── 0002_create_products_orders.sql
└── 0003_add_coupon_to_orders.sql
```

- 개발·테스트·운영 DB에 **같은 순서로** 적용돼서 서로 달라지지 않아요.
- Git에 함께 올라가서 **언제 왜 바뀌었는지** 남아요 (6장).
- 운영 DB에 적용하기 전에는 **반드시 백업** (8장). 칸 삭제·이름 변경은 되돌리기 어려워요.
- 대부분의 프레임워크와 수파베이스가 마이그레이션 기능을 제공해요.

---

## 7. 수파베이스를 쓴다면 — RLS는 필수

57장에서 본 대로, AI 빌더로 만든 앱에서 가장 흔한 사고가 **RLS(행 단위 접근 규칙)를 안 켠 것**이에요.

- 수파베이스는 화면 쪽 코드에서도 DB에 바로 접근할 수 있어요. 그래서 **RLS가 꺼진 표는 누구나 읽고 쓸 수 있어요.**
- 공식 문서 기준: 표 편집기로 만든 표는 RLS가 기본으로 켜지지만, **SQL로 직접 만든 표는 직접 켜야** 해요.

```sql
alter table orders enable row level security;

-- 로그인한 사람은 자기 주문만 볼 수 있다
create policy "본인 주문만 조회"
on orders for select
to authenticated
using ( (select auth.uid()) = user_id );
```

> 💡 Claude에게: "모든 테이블에 RLS가 켜져 있는지, 정책이 없는 테이블이 있는지 확인하고 표로 보여 줘."

---

## 8. AI에게 DB 설계 요청하기

```
작은 쇼핑몰 DB를 설계해 줘.
- 기능: 회원가입, 상품 보기, 장바구니, 주문, 결제, 리뷰
- 돈은 원 단위 정수, 시각은 timestamptz(UTC)
- 주문 항목에는 주문 당시 가격 저장
- 주문·결제는 삭제하지 않고 상태로 관리
먼저 표 목록과 관계를 그림(텍스트)으로 보여 주고, 내가 승인하면 마이그레이션 SQL을 만들어.
자주 쓸 조회 5개와 거기에 필요한 인덱스도 제안해 줘.
```

받은 설계는 **4절 표로 점검**하세요.

---

### 이 장 요약
1. **명사 → 관계 → 칸 → 규칙 → 자주 쓸 조회** 순서로 설계한다. 다 대 다는 **중간 표**로.
2. **돈은 정수(또는 numeric)**, 시각은 **UTC + 시간대 있는 타입**, 주문에는 **당시 가격**, 주문·결제는 **지우지 않고 상태로**.
3. 구조 변경은 **마이그레이션 파일 + 백업**, 수파베이스는 **모든 표에 RLS**.

---

> 📚 이 장의 출처와 확인하지 못한 부분은 [참고 자료 모음](sources.md#5860장-설계모듈화--데이터베이스-설계--api-설계)에 있어요.
