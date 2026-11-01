# 60. API 설계 — 화면과 서버가 대화하는 규칙

> API·JSON·REST 주소 기초는 [코딩 9장](coding/09-web-development.md#4-api와-json--프로그램끼리-대화하기)에 있어요. 이 장은 그다음, **실제 서비스에서 지켜야 할 규칙**이에요.

**API** = 화면(웹·앱)이 서버에게 "상품 목록 줘", "주문 만들어 줘"라고 요청하는 **창구와 규칙**이에요.

식당으로 치면 **메뉴판과 주문서 양식**이에요. 양식이 들쭉날쭉하면 주방(서버)도 손님(화면)도 헷갈려요. 그리고 한번 앱이 손님 휴대폰에 깔리면, 서버 쪽 규칙을 마음대로 바꾸기 어려워요(25장). 그래서 처음부터 일관되게 정해 둬요.

---

## 1. 주소는 명사, 행동은 메서드로

| 메서드 | 뜻 | 예 | 성공 시 상태 코드 |
|---|---|---|---|
| **GET** | 조회 | `GET /api/v1/products` | 200 |
| **POST** | 새로 만들기 | `POST /api/v1/orders` | 201 |
| **PATCH** | 일부 수정 | `PATCH /api/v1/orders/42` | 200 |
| **PUT** | 통째로 바꾸기 | `PUT /api/v1/users/7/address` | 200 |
| **DELETE** | 삭제(또는 취소) | `DELETE /api/v1/cart/items/3` | 204 (돌려줄 내용 없음) |

규칙:
- 주소에는 **명사(복수형)**: `/products`, `/orders` ✕ `/getProducts`, `/createOrder`
- 소속 관계는 경로로: `/users/7/orders` (7번 회원의 주문들)
- 명사로 표현하기 어려운 행동은 예외로 동사를 써도 돼요: `POST /api/v1/orders/42/cancel`
- 이름 규칙(소문자, 하이픈 또는 밑줄)을 **하나로 정하고 끝까지**

---

## 2. 상태 코드 — 결과를 숫자로 알려 주기

| 코드 | 뜻 | 언제 |
|---|---|---|
| **200** OK | 성공 | 조회·수정 성공 |
| **201** Created | 만들어짐 | 주문 생성 성공 |
| **204** No Content | 성공, 내용 없음 | 삭제 성공 |
| **400** Bad Request | 요청 형식이 틀림 | 숫자 자리에 글자 |
| **401** Unauthorized | 로그인 필요 | 로그인 안 함 |
| **403** Forbidden | 권한 없음 | 남의 주문 보기 |
| **404** Not Found | 없음 | 없는 상품 번호 |
| **409** Conflict | 충돌 | 이미 취소된 주문을 또 취소 |
| **422** Unprocessable Content | 형식은 맞지만 내용이 안 됨 | 수량 0개 주문 |
| **429** Too Many Requests | 너무 많이 요청 | 사용량 한도 초과 (41장) |
| **500** Internal Server Error | 서버 잘못 | 버그. 손님 잘못이 아님 |

> 💡 **4로 시작하면 요청한 쪽 문제, 5로 시작하면 서버 문제**예요. 에러인데 200을 보내면 화면이 성공으로 착각해요.

> ⚠️ **남의 데이터 요청에는 403 대신 404를 주기도 해요.** "그런 주문이 있다"는 사실 자체를 숨기려고요. 어느 쪽이든 **서버에서 본인 것인지 반드시 확인**해야 해요(37·50장 "남의 주문 번호 넣어 보기").

---

## 3. 에러는 같은 모양으로 — RFC 9457

에러 응답 모양이 기능마다 다르면 화면 쪽 코드가 복잡해져요. 국제 표준 **RFC 9457 (Problem Details for HTTP APIs, 2023년)**이 정한 모양을 쓰면 편해요.

```json
{
  "type": "about:blank",
  "title": "Not Found",
  "status": 404,
  "detail": "9번 상품이 없어요"
}
```

| 항목 | 뜻 |
|---|---|
| `type` | 문제 종류를 가리키는 주소 (따로 없으면 `about:blank`) |
| `title` | 짧은 제목 |
| `status` | 상태 코드 (실제 응답 코드와 같아야 함) |
| `detail` | 이번 경우의 설명 |
| `instance` | (선택) 이번 사건을 가리키는 값 |

- 응답 형식(Content-Type)은 `application/problem+json`.
- 입력 칸별 오류 목록처럼 **필요한 항목은 직접 추가**해도 돼요(표준이 허용).
- **에러 메시지에 내부 정보를 넣지 마세요**: DB 오류 원문, 서버 경로, 비밀 키 등 (37장).

---

## 4. 목록은 나눠서 주기 — 페이지네이션

상품이 1만 개인데 한 번에 다 보내면 느리고 비싸요. 나눠서 줘요.

| 방식 | 요청 예 | 장점 | 단점 |
|---|---|---|---|
| **번호(offset)** | `?page=3&limit=20` | 쉬움, "3페이지로 가기" 가능 | 중간에 새 글이 생기면 **중복·누락**, 뒤 페이지일수록 느림 |
| **커서(cursor)** | `?limit=20&starting_after=1234` | 데이터가 바뀌어도 안정, 빠름 | 특정 페이지로 바로 가기 어려움 |

- 게시판·관리자 화면: 번호 방식으로 시작해도 충분
- 무한 스크롤·피드·주문 내역: **커서 방식**
- 예: 스트라이프 API는 `starting_after`·`ending_before`(마지막으로 받은 항목 번호)와 `limit`(1~100)을 써요.
- 응답에 **다음이 더 있는지**(`has_more`)를 넣어 줘요.

---

## 5. 두 번 눌러도 한 번만 — 멱등성 키

결제·주문처럼 **두 번 실행되면 사고**인 요청은, 화면이 요청마다 **고유한 키**를 붙여 보내고 서버는 같은 키가 또 오면 **새로 만들지 않고 처음 결과를 돌려줘요.**

```
POST /api/v1/orders
Idempotency-Key: 2f1c9a7e-...(요청마다 새로 만든 무작위 값)
```

- 스트라이프 공식 문서 기준: 처음 요청의 결과(성공이든 실패든)를 저장해 두고, 같은 키로 다시 오면 그 결과를 돌려줘요. 키는 **최소 24시간** 뒤에 지워질 수 있고, 무작위 값(UUID v4)을 권장해요.
- GET·DELETE는 원래 여러 번 해도 결과가 같아서 키가 필요 없어요.
- 네트워크가 끊겨 화면이 **"됐는지 모르겠다"**며 다시 보낼 때 특히 중요해요 (39장 결제, 50장 "두 번 클릭" 테스트).

---

## 6. 실습 — 작은 API 서버 만들어 보기

파이썬 기본 기능만으로 위 규칙(주소, 상태 코드, 에러 모양, 멱등성 키)을 담은 서버예요.

```python
# api.py
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

PRODUCTS = {1: {"id": 1, "name": "그래놀라", "price": 12900}}
ORDERS = {}          # 주문 번호 → 주문
SEEN_KEYS = {}       # 멱등성 키 → 처음 만든 주문

class Api(BaseHTTPRequestHandler):
    def send_json(self, status, body, content_type="application/json"):
        data = json.dumps(body, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        self.wfile.write(data)

    def problem(self, status, title, detail):
        self.send_json(status, {"type": "about:blank", "title": title,
                                "status": status, "detail": detail},
                       "application/problem+json")

    def do_GET(self):
        parts = self.path.strip("/").split("/")      # api, v1, products, 1
        if parts[:3] != ["api", "v1", "products"]:
            return self.problem(404, "Not Found", "없는 주소예요")
        if len(parts) == 3:
            return self.send_json(200, {"data": list(PRODUCTS.values())})
        if not parts[3].isdigit():
            return self.problem(400, "Bad Request", "상품 번호는 숫자여야 해요")
        product = PRODUCTS.get(int(parts[3]))
        if not product:
            return self.problem(404, "Not Found", f"{parts[3]}번 상품이 없어요")
        self.send_json(200, product)

    def do_POST(self):
        if self.path != "/api/v1/orders":
            return self.problem(404, "Not Found", "없는 주소예요")
        key = self.headers.get("Idempotency-Key")
        if not key:
            return self.problem(400, "Bad Request", "Idempotency-Key 헤더가 필요해요")
        if key in SEEN_KEYS:                          # 같은 요청이 또 오면
            return self.send_json(200, SEEN_KEYS[key])  # 새로 만들지 않고 처음 결과를 돌려줌
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        product = PRODUCTS.get(body.get("product_id"))
        if not product or body.get("qty", 0) <= 0:
            return self.problem(422, "Unprocessable Content", "상품 번호나 수량이 잘못됐어요")
        order = {"id": len(ORDERS) + 1, "total": product["price"] * body["qty"]}
        ORDERS[order["id"]] = order
        SEEN_KEYS[key] = order
        self.send_json(201, order)

    def log_message(self, *args):
        pass

if __name__ == "__main__":
    HTTPServer(("127.0.0.1", 8000), Api).serve_forever()
```

이 서버에 요청을 보내 본 결과 (테스트 코드로 직접 확인했어요):

| 요청 | 결과 |
|---|---|
| `GET /api/v1/products` | **200** `{"data": [{"id": 1, "name": "그래놀라", "price": 12900}]}` |
| `GET /api/v1/products/9` | **404** `{"type": "about:blank", "title": "Not Found", "status": 404, "detail": "9번 상품이 없어요"}` |
| `GET /api/v1/products/abc` | **400** `... "detail": "상품 번호는 숫자여야 해요"` |
| `POST /api/v1/orders` 수량 2, 키 `abc-123` | **201** `{"id": 1, "total": 25800}` |
| 같은 요청을 **같은 키로 한 번 더** | **200** `{"id": 1, "total": 25800}` → 주문은 **1개만** 생김 |
| `POST /api/v1/orders` 수량 0 | **422** `... "detail": "상품 번호나 수량이 잘못됐어요"` |

> ⚠️ 연습용이라 저장을 메모리에 해요(서버를 끄면 사라짐). 실제 서비스에서는 프레임워크(FastAPI, Express 등)와 DB를 쓰고, 로그인 확인·입력 검사·사용량 제한을 더해야 해요. **구조와 규칙을 익히는 용도**로만 쓰세요.

직접 해 보기: `python3 api.py`로 켜고, 다른 터미널에서
```bash
curl -i http://127.0.0.1:8000/api/v1/products/9
curl -i -X POST http://127.0.0.1:8000/api/v1/orders \
  -H "Content-Type: application/json" -H "Idempotency-Key: abc-123" \
  -d '{"product_id": 1, "qty": 2}'
```

---

## 7. 그 밖에 정해 둘 것

| 항목 | 권장 |
|---|---|
| **버전** | 주소에 `/api/v1/`. 기존 앱이 깨지는 변경은 `v2`로 (칸 **추가**는 괜찮고, 칸 **삭제·이름 변경**은 깨짐) |
| **인증** | 로그인 정보는 헤더(`Authorization`)나 안전한 쿠키로. **주소에 토큰·비밀 키를 넣지 않기** (로그에 남음) |
| **권한 확인** | 모든 요청에서 **서버가** "이 사람 것인가" 확인. 화면에서 버튼을 숨기는 건 보안이 아님 |
| **입력 검사** | 서버에서 다시 검사 (화면 검사는 편의용). 금액은 **서버가 DB 가격으로 계산** (39장) |
| **사용량 제한** | 로그인·문자 발송·AI 호출은 1분당 횟수 제한, 넘으면 429 (41장) |
| **이름 규칙** | JSON 칸 이름은 `snake_case` 또는 `camelCase` 중 **하나로 통일** |
| **시각** | `2026-11-01T09:00:00Z`처럼 **ISO 8601 + UTC** (59장) |
| **돈** | 정수(원 단위)로, 통화가 여러 개면 `{"amount": 12900, "currency": "KRW"}` |
| **문서** | **OpenAPI**(API 설명 표준 형식) 파일로 정리하면 문서 화면·테스트를 자동으로 만들 수 있어요 |
| **웹훅** | 결제 회사 등이 **내 서버로** 알려 주는 요청. 서명 검증 + 같은 알림 중복 처리 (39장) |

---

## 8. AI에게 API 설계 요청하기

```
쇼핑몰 API를 설계해 줘. 코드보다 먼저 표로 보여 줘.
- 주소는 /api/v1/ 아래, 명사 복수형
- 각 API마다: 메서드, 주소, 로그인 필요 여부, 요청 예, 성공 응답과 상태 코드, 에러 경우
- 에러는 RFC 9457 형식(application/problem+json)으로 통일
- 주문·결제 생성은 Idempotency-Key 헤더 필수
- 목록은 커서 방식 페이지네이션 (limit, starting_after, has_more)
- 모든 API에서 본인 데이터인지 서버가 확인
내가 승인하면 OpenAPI 파일과 코드를 만들어.
```

출시 전 점검 요청:
> "모든 API를 표로 정리하고, ① 로그인 확인이 없는 것 ② 본인 데이터인지 확인하지 않는 것 ③ 화면에서 보낸 금액을 그대로 믿는 것 ④ 에러에 내부 정보가 나오는 것을 찾아 줘."

---

### 이 장 요약
1. 주소는 **명사**, 행동은 **메서드**, 결과는 **상태 코드**로. 4xx는 요청 쪽, 5xx는 서버 쪽 문제.
2. 에러는 **RFC 9457 한 모양**으로, 목록은 **페이지네이션**, 결제·주문은 **멱등성 키**로 중복을 막는다.
3. **버전(/v1)**, **서버에서 권한·금액 확인**, **사용량 제한**, **OpenAPI 문서**를 처음부터 정해 둔다.

---

> 📚 이 장의 출처와 확인하지 못한 부분은 [참고 자료 모음](sources.md#5860장-설계모듈화--데이터베이스-설계--api-설계)에 있어요.
