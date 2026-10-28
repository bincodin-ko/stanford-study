# 13. 연습 문제와 퀴즈

먼저 직접 풀어 보고, 정답은 **[정답 보기]** 를 눌러 확인하세요. 코드 문제의 정답은 한 가지 예시일 뿐이고, 다르게 풀어도 결과가 같으면 정답이에요.

---

## A. 개념 퀴즈

**Q1.** 실행 전에 코드 전체를 기계어로 미리 번역하는 방식은? 대표 언어 2개는?

<details><summary>정답 보기</summary>컴파일 방식. C, C++, Go, 러스트 중 2개. (1장)</details>

**Q2.** 자바와 자바스크립트는 같은 언어인가요?

<details><summary>정답 보기</summary>아니요. 이름만 비슷한 완전히 다른 언어예요. (2장)</details>

**Q3.** 유니티로 게임을 만들 때 주로 쓰는 언어는? 안드로이드 공식 권장 언어는?

<details><summary>정답 보기</summary>C# / 코틀린. (2장)</details>

**Q4.** HTML과 CSS가 보통 "프로그래밍 언어"로 분류되지 않는 이유는?

<details><summary>정답 보기</summary>계산이나 조건 판단 같은 "명령 실행"을 하지 못하고, 웹 페이지의 구조(HTML)와 모양(CSS)을 표현하기 때문. (2장)</details>

**Q5.** 파이썬에서 `print("3" + "4")`와 `print(3 + 4)`의 결과는?

<details><summary>정답 보기</summary><code>34</code> (글자 이어 붙이기) / <code>7</code> (숫자 더하기). (4장)</details>

**Q6.** `range(1, 5)`에 들어 있는 숫자는?

<details><summary>정답 보기</summary>1, 2, 3, 4 (끝 숫자 5는 포함하지 않음). (4장)</details>

**Q7.** 리스트 `["a", "b", "c"]`에서 `"c"`의 번호(인덱스)는?

<details><summary>정답 보기</summary>2 (0부터 시작). <code>-1</code>로도 꺼낼 수 있어요. (5장)</details>

**Q8.** 오류 메시지는 어디부터 읽어야 하나요?

<details><summary>정답 보기</summary>맨 아래 줄(오류 종류와 내용)부터. 그다음 줄 번호를 보고 해당 줄로 간다. (5장)</details>

**Q9.** 클래스와 객체의 관계를 붕어빵으로 설명하면?

<details><summary>정답 보기</summary>클래스 = 붕어빵 틀(설계도), 객체 = 틀로 찍어 낸 붕어빵 하나하나. (6장)</details>

**Q10.** 데이터 100만 개에서 O(n²) 알고리즘과 O(n log n) 알고리즘 중 어느 쪽이 빠른가요?

<details><summary>정답 보기</summary>O(n log n). 대략 1조 번 vs 2천만 번 수준의 차이. (7장)</details>

**Q11.** "뒤로 가기", "실행 취소"에 어울리는 자료구조는? "주문 대기열"은?

<details><summary>정답 보기</summary>스택(나중에 넣은 게 먼저) / 큐(먼저 온 게 먼저). (7장)</details>

**Q12.** 이진 탐색을 쓰려면 데이터가 어떤 상태여야 하나요?

<details><summary>정답 보기</summary>정렬되어 있어야 한다. (7장)</details>

**Q13.** HTTP 상태 코드 404와 500의 차이는?

<details><summary>정답 보기</summary>404: 요청한 페이지가 없음(손님 쪽 문제) / 500: 서버 내부 오류(서버 쪽 문제). (9장)</details>

**Q14.** SQL에서 `DELETE FROM products;` 를 실행하면 어떻게 되나요?

<details><summary>정답 보기</summary><code>WHERE</code>가 없어서 products 표의 <b>모든 행</b>이 지워진다. (9장)</details>

**Q15.** 손님이 입력한 값을 SQL 문장에 그대로 이어 붙이면 생기는 보안 문제는?

<details><summary>정답 보기</summary>SQL 인젝션. 자리표시자(<code>?</code>)로 값을 따로 넘겨서 막는다. (9장)</details>

**Q16.** 메모리를 자동으로 치워 주는 장치를 무엇이라 하나요? 이 장치가 없는 대표 언어는?

<details><summary>정답 보기</summary>가비지 컬렉터(GC). C, C++ (러스트는 GC 대신 소유권 규칙). (10장)</details>

**Q17.** 재고 1개 남은 상품을 두 사람이 동시에 결제해서 재고가 -1이 되는 문제를 무엇이라 하나요?

<details><summary>정답 보기</summary>경쟁 상태(race condition). 락, DB 트랜잭션으로 막는다. (10장)</details>

**Q18.** 성능 최적화의 첫 단계는?

<details><summary>정답 보기</summary>측정(어디가 느린지 프로파일러로 확인). 추측으로 고치지 않는다. (10장)</details>

**Q19.** YAGNI 원칙의 뜻은?

<details><summary>정답 보기</summary>"지금 필요 없는 기능은 만들지 마라(You Aren't Gonna Need It)". (11장)</details>

**Q20.** AI 코딩 도구를 쓸 때 사람에게 남는 책임 3가지는?

<details><summary>정답 보기</summary>설계 판단, 결과 검증(테스트·리뷰), 최종 책임. 요구사항 이해도 포함. (8·11장)</details>

---

## B. 코딩 문제 (파이썬)

### 🟢 입문

**P1.** 1부터 100까지 중 **3의 배수의 합**을 출력하세요.

<details><summary>정답 보기</summary>

```python
total = 0
for i in range(1, 101):
    if i % 3 == 0:
        total += i
print(total)    # 1683
```
</details>

**P2.** 점수 리스트 `[72, 95, 88, 61, 79]`의 **평균, 최고점, 최저점**을 출력하세요.

<details><summary>정답 보기</summary>

```python
scores = [72, 95, 88, 61, 79]
print(sum(scores) / len(scores))   # 79.0
print(max(scores))                 # 95
print(min(scores))                 # 61
```
</details>

**P3.** 문자열을 받아 **거꾸로 뒤집어** 돌려주는 함수 `reverse_text`를 만드세요. (`"코딩"` → `"딩코"`)

<details><summary>정답 보기</summary>

```python
def reverse_text(text):
    return text[::-1]       # 처음부터 끝까지, -1칸씩(거꾸로)

print(reverse_text("코딩"))     # 딩코
print(reverse_text("hello"))   # olleh
```
</details>

### 🟡 초급

**P4.** 문장에서 **단어별 등장 횟수**를 세는 함수를 만드세요.

<details><summary>정답 보기</summary>

```python
def word_count(sentence):
    counts = {}
    for word in sentence.split():
        counts[word] = counts.get(word, 0) + 1
    return counts

print(word_count("나는 사과 좋아 너는 사과 싫어"))
# {'나는': 1, '사과': 2, '좋아': 1, '너는': 1, '싫어': 1}
```
</details>

**P5.** **FizzBuzz**: 1~15를 출력하되, 3의 배수는 `Fizz`, 5의 배수는 `Buzz`, 둘 다면 `FizzBuzz`. (개발자 면접에서 유명한 문제)

<details><summary>정답 보기</summary>

```python
for i in range(1, 16):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```
15의 배수를 <b>가장 먼저</b> 검사하는 게 핵심이에요.
</details>

**P6.** 앞뒤가 같은 단어(**회문**, 예: "기러기", "level")인지 확인하는 함수를 만드세요.

<details><summary>정답 보기</summary>

```python
def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("기러기"))   # True
print(is_palindrome("코딩"))     # False
```
</details>

### 🟠 중급

**P7.** `Product` 클래스(이름·가격)와, 상품을 담고 **총액**을 계산하는 `Cart` 클래스를 만드세요. 3만 원 이상이면 배송비 0원, 아니면 3,000원.

<details><summary>정답 보기</summary>

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    FREE_SHIPPING_MIN = 30000
    SHIPPING_FEE = 3000

    def __init__(self):
        self.items = []

    def add(self, product, quantity=1):
        self.items.append((product, quantity))

    def subtotal(self):
        return sum(p.price * q for p, q in self.items)

    def total(self):
        sub = self.subtotal()
        shipping = 0 if sub >= self.FREE_SHIPPING_MIN else self.SHIPPING_FEE
        return sub + shipping

cart = Cart()
cart.add(Product("그래놀라", 12900), 2)
print(cart.total())     # 28800 (상품 25800 + 배송비 3000)
cart.add(Product("쿠키", 3000))
print(cart.total())     # 31800 (상품 28800원 — 아직 3만 원 미만이라 배송비 3000원 포함)
```
</details>

**P8.** 괄호 문자열이 올바르게 짝지어졌는지 **스택**으로 확인하세요. (`"(())"` → True, `"(()"` → False, `")("` → False)

<details><summary>정답 보기</summary>

```python
def is_valid(brackets):
    stack = []
    for ch in brackets:
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

print(is_valid("(())"))   # True
print(is_valid("(()"))    # False
print(is_valid(")("))     # False
```
</details>

### 🔴 고급

**P9.** 미로에서 시작(S)부터 도착(E)까지 **최단 거리**를 BFS로 구하세요. `#`은 벽.

<details><summary>정답 보기</summary>

```python
from collections import deque

maze = [
    "S.#.",
    "..#.",
    "...E",
]

def shortest_path(maze):
    rows, cols = len(maze), len(maze[0])
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == "S":
                start = (r, c)
    queue = deque([(start, 0)])
    visited = {start}
    while queue:
        (r, c), dist = queue.popleft()
        if maze[r][c] == "E":
            return dist
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != "#" and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), dist + 1))
    return -1

print(shortest_path(maze))    # 5
```
가까운 칸부터 퍼져 나가기 때문에, 처음 E에 닿았을 때의 거리가 곧 최단 거리예요. (7장)
</details>

**P10.** 오목에서 마지막에 둔 돌을 기준으로 **5개가 연속**됐는지 확인하는 함수를 만드세요. (사업 20장 오목 서버의 핵심 판정 로직)

<details><summary>정답 보기</summary>

```python
def is_five(board, row, col):
    stone = board[row][col]
    size = len(board)
    for dr, dc in [(0, 1), (1, 0), (1, 1), (1, -1)]:   # 가로, 세로, 대각선 2개
        count = 1
        for sign in (1, -1):                          # 양쪽 방향으로 세기
            r, c = row + dr * sign, col + dc * sign
            while 0 <= r < size and 0 <= c < size and board[r][c] == stone:
                count += 1
                r += dr * sign
                c += dc * sign
        if count >= 5:
            return True
    return False

board = [["." for _ in range(15)] for _ in range(15)]
for c in range(3, 8):
    board[7][c] = "B"           # 7행 3~7열에 흑돌 5개
print(is_five(board, 7, 5))     # True
board[0][0] = "W"               # 구석에 백돌 하나
print(is_five(board, 0, 0))     # False
```
이 함수는 <b>방금 돌을 둔 칸</b>을 넣어서 부르는 게 전제예요(빈칸을 넣으면 빈칸끼리 세게 돼요). 렌주룰(장목 금지 등)을 적용하려면 <code>count == 5</code> 처럼 조건을 바꾸면 돼요.
</details>

---

## C. 프로젝트 과제 (단계별)

| 단계 | 과제 | 쓰는 지식 |
|---|---|---|
| 입문 | 숫자 맞히기 게임 (4장) | 변수·조건·반복 |
| 초급 | 가계부 CSV 프로그램 (5장) | 리스트·딕셔너리·파일 |
| 초급 | 자기소개 웹페이지 배포 (9장) | HTML·CSS·GitHub Pages |
| 중급 | 할 일 목록 웹앱 + 서버 + DB (9장) | JS·API·SQL |
| 중급 | 로또 번호 통계 사이트 (사업 19장 🟢 버전) | 데이터 수집·시각화·"재미용" 표시 |
| 고급 | 실시간 1:1 오목 (사업 20장) | 웹소켓·서버 판정·BFS/탐색 AI |
| 고수 | 위 서비스를 배포하고 모니터링·백업·장애 대응까지 운영 (사업 6~9장) | 전부 |
