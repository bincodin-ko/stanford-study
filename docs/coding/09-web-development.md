# 09. 웹 개발 실전

배운 걸 모아서 **실제 웹 서비스**를 만드는 방법이에요. [사업 5장(사이트 구조)](../05-how-websites-work.md)과 같이 보면 좋아요.

---

## 1. 웹이 움직이는 방식 — 요청과 응답

```
브라우저(손님)                         서버(가게)
   │ ── 요청(Request) ──────────────▶ │  "GET /products 상품 목록 주세요"
   │                                  │  → 데이터베이스에서 꺼냄
   │ ◀────────────── 응답(Response) ── │  "200 OK + 상품 목록"
```

### HTTP — 브라우저와 서버의 대화 규칙
| 요청 종류(메서드) | 뜻 | 예 |
|---|---|---|
| **GET** | 가져오기 | 상품 목록 보기 |
| **POST** | 새로 만들기 | 회원가입, 주문하기 |
| **PUT / PATCH** | 고치기 | 주소 변경 |
| **DELETE** | 지우기 | 장바구니에서 빼기 |

| 응답 번호(상태 코드) | 뜻 |
|---|---|
| **200** | 성공 |
| **201** | 새로 만들어짐 |
| **301 / 302** | 다른 주소로 이동하세요 |
| **400** | 요청이 이상해요 (손님 잘못) |
| **401 / 403** | 로그인 필요 / 권한 없음 |
| **404** | 그런 페이지 없어요 |
| **500** | 서버가 고장 났어요 (서버 잘못) |

> 외우는 팁: **2xx 성공, 3xx 이동, 4xx 손님 쪽 문제, 5xx 서버 쪽 문제.**

---

## 2. 프론트엔드 — 손님이 보는 화면

세 가지가 함께 일해요.

```html
<!-- index.html : 뼈대 (HTML) -->
<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <title>카운터</title>
  <style>
    /* 모양 (CSS) */
    body { font-family: sans-serif; text-align: center; margin-top: 80px; }
    button { font-size: 24px; padding: 8px 24px; }
  </style>
</head>
<body>
  <h1 id="count">0</h1>
  <button id="plus">+1</button>

  <script>
    // 움직임 (자바스크립트)
    let count = 0;
    document.getElementById("plus").addEventListener("click", () => {
      count += 1;
      document.getElementById("count").textContent = count;
    });
  </script>
</body>
</html>
```
이 내용을 `index.html`로 저장하고 브라우저로 열면 버튼을 누를 때마다 숫자가 올라가요.

### 프론트엔드 프레임워크
화면이 복잡해지면 **React, Vue, Svelte, Angular** 같은 프레임워크(뼈대 도구)를 써요. 요즘은 React + 타입스크립트 조합이 가장 흔해요.

---

## 3. 백엔드 — 보이지 않는 서버

### 파이썬 표준 라이브러리만으로 만든 아주 작은 서버
```python
# server.py — 실행: python3 server.py → 브라우저에서 http://localhost:8000/api/products
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

PRODUCTS = [
    {"id": 1, "name": "쿠키", "price": 3000},
    {"id": 2, "name": "그래놀라", "price": 12900},
]

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/products":
            body = json.dumps(PRODUCTS, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self.end_headers()

HTTPServer(("localhost", 8000), Handler).serve_forever()
```

실무에서는 이런 일을 대신해 주는 **백엔드 프레임워크**를 써요.

| 언어 | 대표 프레임워크 |
|---|---|
| 파이썬 | FastAPI, Django, Flask |
| 자바스크립트/타입스크립트 | Express, NestJS, Next.js(화면+서버) |
| 자바 / 코틀린 | **Spring Boot** (한국 기업에서 매우 많이 씀) |
| Go | Gin, 표준 라이브러리 |
| PHP | Laravel |
| 루비 | Ruby on Rails |
| C# | ASP.NET Core |

---

## 4. API와 JSON — 프로그램끼리 대화하기

- **API** = 프로그램이 다른 프로그램에게 기능을 제공하는 창구.
- **JSON** = 데이터를 주고받는 형식. 5장의 "리스트 + 딕셔너리"와 거의 같은 모양.
```json
[
  {"id": 1, "name": "쿠키", "price": 3000},
  {"id": 2, "name": "그래놀라", "price": 12900}
]
```

### 화면(JS)에서 서버 API 부르기
```javascript
const res = await fetch("/api/products");
const products = await res.json();
products.forEach(p => console.log(p.name, p.price));
```

### REST API 주소 설계 관례
| 요청 | 주소 | 뜻 |
|---|---|---|
| GET | `/api/products` | 상품 목록 |
| GET | `/api/products/2` | 2번 상품 |
| POST | `/api/products` | 상품 추가 |
| PATCH | `/api/products/2` | 2번 상품 수정 |
| DELETE | `/api/products/2` | 2번 상품 삭제 |

---

## 5. 데이터베이스와 SQL

데이터베이스 = 서비스의 장부(사업 5장). 가장 많이 쓰는 건 **표(테이블)** 로 저장하는 **관계형 데이터베이스(RDB)** 예요.
예: MySQL, PostgreSQL, SQLite, Oracle

| id | name | price |
|---|---|---|
| 1 | 쿠키 | 3000 |
| 2 | 그래놀라 | 12900 |

### SQL 기본 4가지 (CRUD)
```sql
-- 만들기(Create)
INSERT INTO products (name, price) VALUES ('주스', 4500);

-- 읽기(Read)
SELECT name, price FROM products WHERE price < 10000 ORDER BY price;

-- 고치기(Update)
UPDATE products SET price = 3500 WHERE name = '쿠키';

-- 지우기(Delete)
DELETE FROM products WHERE id = 3;
```
> ⚠️ `UPDATE`와 `DELETE`에서 `WHERE`를 빼먹으면 **표 전체**가 바뀌거나 지워져요. 실무 대형 사고 단골이라, 운영 DB에서는 먼저 `SELECT`로 대상부터 확인하고, 백업(사업 8장)을 꼭 해 두세요.

### 파이썬에서 SQL 쓰기 (SQLite, 설치 불필요)
```python
import sqlite3

conn = sqlite3.connect(":memory:")       # 메모리 안에 임시 DB 만들기
cur = conn.cursor()
cur.execute("CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price INTEGER)")
cur.executemany("INSERT INTO products (name, price) VALUES (?, ?)",
                [("쿠키", 3000), ("그래놀라", 12900), ("주스", 4500)])

max_price = 5000
cur.execute("SELECT name, price FROM products WHERE price < ? ORDER BY price", (max_price,))
for name, price in cur.fetchall():
    print(name, price)
# 쿠키 3000
# 주스 4500
conn.close()
```

### `?` 를 쓰는 이유 — SQL 인젝션 막기
```python
# ❌ 절대 이렇게 하지 마세요: 손님이 입력한 글자를 SQL에 그대로 붙이기
# cur.execute(f"SELECT * FROM users WHERE name = '{user_input}'")
#   → 손님이 이름 칸에 ' OR '1'='1 을 넣으면 모든 회원 정보가 나옴

# ✅ 항상 자리표시자(?)로 값을 따로 넘기기
# cur.execute("SELECT * FROM users WHERE name = ?", (user_input,))
```
[사업 10장 보안](../10-security-and-law.md)의 "SQL 인젝션"이 바로 이것이에요.

### 인덱스 — DB의 책갈피
- 자주 검색하는 칸에 **인덱스**를 만들면 찾기가 O(n) → O(log n) 수준으로 빨라져요 (7장의 트리 구조).
- 대신 데이터를 넣을 때 조금 느려지고 공간을 더 씀.

### NoSQL
- 표 대신 문서(JSON)·키-값·그래프 형태로 저장: MongoDB, Redis(캐시), Firebase 등.

---

## 6. 로그인과 보안 기본

| 항목 | 해야 할 것 |
|---|---|
| 비밀번호 저장 | **해시(bcrypt, argon2 등)** 로 저장. 원래 비밀번호를 저장하지 않음 |
| 로그인 상태 유지 | 세션 쿠키 또는 토큰(JWT 등) |
| HTTPS | 모든 통신 암호화 |
| 입력값 | 서버에서 다시 검사 (화면에서 막아도 서버를 직접 부를 수 있음) |
| 권한 | "로그인했나?" + "이 데이터의 주인인가?" 둘 다 확인 |

---

## 7. 배포 — 내 컴퓨터 → 인터넷

```
내 컴퓨터에서 개발 → GitHub에 push → (자동 테스트) → 서버에 배포 → 도메인 연결
```
- 쉬운 배포 플랫폼: Vercel, Netlify(화면), Render, Railway, Fly.io(서버) 등
- 클라우드: AWS, 구글 클라우드, 애저, 네이버 클라우드
- **도커(Docker)**: 프로그램과 실행 환경을 **상자(컨테이너)** 에 통째로 담아서, 어디서든 똑같이 실행되게 하는 도구. "내 컴퓨터에선 되는데요?" 문제를 줄여 줘요.

운영·백업·모니터링은 [사업 6~9장](../06-environments-and-git.md)에 자세히 있어요.

---

## 8. 첫 웹 프로젝트 추천 순서

1. **HTML/CSS로 자기소개 페이지** → GitHub Pages로 무료 배포
2. **자바스크립트로 할 일 목록(To-do)** — 추가·삭제·완료 표시
3. **할 일 목록을 서버 + DB에 저장** (FastAPI/Express + SQLite)
4. **로그인 추가**
5. **배포 + 도메인 연결**

여기까지 하면 "웹 서비스를 혼자 처음부터 끝까지 만들어 본 사람"이 됩니다.

---

### 이 장 요약
1. 웹 = **요청(GET/POST…)과 응답(200/404/500…)**.
2. 프론트엔드는 **HTML(뼈대)·CSS(모양)·JS(움직임)**, 백엔드는 **API + DB**.
3. SQL은 **CRUD**, `WHERE` 빼먹지 않기, 손님 입력은 **항상 자리표시자(?)** 로.
