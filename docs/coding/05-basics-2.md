# 05. 기초 ②: 데이터 묶음 · 문자열 · 파일 · 오류

4장의 뼈대에 **"여러 값을 한 번에 다루는 법"** 과 **"현실의 일(파일, 오류)"** 을 더하면, 실제로 쓸 만한 도구를 만들 수 있어요.

---

## 1. 리스트 — 순서 있는 목록

```python
fruits = ["사과", "바나나", "포도"]

print(fruits[0])        # 사과   ← 번호(인덱스)는 0부터 시작!
print(fruits[-1])       # 포도   ← -1은 맨 뒤
print(len(fruits))      # 3      길이(개수)

fruits.append("딸기")    # 맨 뒤에 추가
fruits.remove("바나나")  # 값으로 삭제
print(fruits)           # ['사과', '포도', '딸기']

for f in fruits:        # 하나씩 꺼내 반복
    print(f, "맛있다")
```

> ⚠️ **번호가 0부터 시작**하는 건 거의 모든 언어 공통이에요. 3개짜리 리스트의 마지막 번호는 2. 없는 번호(`fruits[10]`)를 쓰면 오류가 나요.

### 잘라 쓰기(슬라이싱)
```python
nums = [10, 20, 30, 40, 50]
print(nums[1:3])     # [20, 30]   1번부터 3번 "전"까지
print(nums[:2])      # [10, 20]   처음부터 2개
print(sum(nums))     # 150
print(max(nums))     # 50
```

### 리스트 컴프리헨션 (짧게 만들기)
```python
squares = [n * n for n in range(1, 6)]
print(squares)                         # [1, 4, 9, 16, 25]

evens = [n for n in range(10) if n % 2 == 0]
print(evens)                           # [0, 2, 4, 6, 8]
```

---

## 2. 딕셔너리 — 이름(키)으로 찾는 사전

```python
person = {"name": "민수", "age": 20, "city": "서울"}

print(person["name"])        # 민수
person["age"] = 21           # 값 바꾸기
person["job"] = "학생"        # 새 항목 추가

for key, value in person.items():
    print(key, ":", value)

print("city" in person)      # True   키가 있는지 확인
print(person.get("phone", "없음"))   # 없음   (없는 키를 안전하게 꺼내기)
```

### 리스트 vs 딕셔너리
| | 리스트 | 딕셔너리 |
|---|---|---|
| 찾는 방법 | 번호로 `[0]` | 이름(키)으로 `["name"]` |
| 어울리는 데이터 | 순서가 중요한 목록 (장바구니, 순위) | 항목마다 이름이 있는 정보 (회원 정보, 설정) |

### 둘을 섞으면 = 실제 데이터 모양
```python
products = [
    {"name": "쿠키", "price": 3000},
    {"name": "그래놀라", "price": 12900},
    {"name": "주스", "price": 4500},
]

cheap = [p["name"] for p in products if p["price"] < 5000]
print(cheap)       # ['쿠키', '주스']
```
> 이 모양이 웹에서 데이터를 주고받는 **JSON**과 거의 똑같아요 (9장).

### 그 밖의 묶음
- **튜플** `(1, 2)`: 바꿀 수 없는 리스트
- **집합(set)** `{1, 2, 3}`: 중복 없는 모음. `set([1, 1, 2])` → `{1, 2}`

---

## 3. 문자열 다루기

```python
text = "  Hello, Python!  "

print(text.strip())          # "Hello, Python!"   양쪽 공백 제거
print(text.lower())          # 소문자로
print(text.replace("Python", "코딩"))
print("Python" in text)      # True

words = "사과,바나나,포도".split(",")
print(words)                 # ['사과', '바나나', '포도']
print("-".join(words))       # 사과-바나나-포도

name = "민수"
age = 20
print(f"{name}님은 {age}살입니다")      # f-문자열: 변수를 글자 안에 바로 넣기
print(f"가격: {12900:,}원")             # 가격: 12,900원  (천 단위 쉼표)
```

---

## 4. 파일 읽고 쓰기

```python
# 쓰기 ("w" = write, 덮어쓰기)
with open("memo.txt", "w", encoding="utf-8") as f:
    f.write("첫 줄\n")
    f.write("둘째 줄\n")

# 이어 쓰기 ("a" = append)
with open("memo.txt", "a", encoding="utf-8") as f:
    f.write("셋째 줄\n")

# 읽기 ("r" = read)
with open("memo.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

- `with` 를 쓰면 다 쓰고 나서 **파일을 자동으로 닫아** 줘요.
- `encoding="utf-8"` → 한글이 깨지지 않게.
- ⚠️ `"w"` 는 **기존 내용을 지우고** 새로 써요. (사업 8장: 덮어쓰기 전에 백업!)

### CSV(엑셀 표) 다루기
```python
import csv

with open("scores.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["이름", "점수"])
    writer.writerow(["민수", 85])
    writer.writerow(["지영", 92])

with open("scores.csv", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

total = sum(int(r["점수"]) for r in rows)
print("평균:", total / len(rows))     # 평균: 88.5
```

---

## 5. 오류(에러) 읽는 법과 처리하기

### 오류 메시지는 "어디서, 무엇이" 잘못됐는지 알려 주는 친절한 편지
```
Traceback (most recent call last):
  File "test.py", line 3, in <module>
    print(10 / 0)
ZeroDivisionError: division by zero
```
- **맨 아래 줄부터 읽기**: `ZeroDivisionError` = 0으로 나눴다
- **line 3**: 3번째 줄에서 났다

### 자주 보는 오류
| 오류 | 뜻 | 흔한 원인 |
|---|---|---|
| `SyntaxError` | 문법 오류 | 괄호·따옴표·콜론(`:`) 빠짐 |
| `IndentationError` | 들여쓰기 오류 | 띄어쓰기 칸 수가 안 맞음 |
| `NameError` | 그런 이름 없음 | 변수 이름 오타, 만들기 전에 사용 |
| `TypeError` | 자료형이 안 맞음 | `"10" + 5` (글자 + 숫자) |
| `ValueError` | 값이 이상함 | `int("abc")` |
| `IndexError` | 번호 범위 밖 | 3개짜리 리스트에서 `[5]` |
| `KeyError` | 그런 키 없음 | 딕셔너리에 없는 키 |
| `FileNotFoundError` | 파일 없음 | 경로 오타 |

### `try / except` — 오류가 나도 프로그램이 죽지 않게
```python
text = "abc"
try:
    number = int(text)
    print("숫자:", number)
except ValueError:
    print("숫자가 아니에요. 다시 입력하세요.")
# 출력: 숫자가 아니에요. 다시 입력하세요.
```

> 💡 **오류가 났을 때 할 일 순서**: ① 맨 아래 줄 읽기 ② 줄 번호로 가기 ③ 그 줄의 변수 값을 `print`로 찍어 보기 ④ 오류 메시지를 그대로 검색하거나 AI에게 물어보기 (8장 디버깅).

---

## 6. 모듈과 라이브러리 — 남이 만든 기능 빌려 쓰기

```python
import math
print(math.sqrt(16))        # 4.0  제곱근

import random
print(random.choice(["가위", "바위", "보"]))

from datetime import date
print(date.today())         # 오늘 날짜
```

- **표준 라이브러리**: 파이썬에 기본으로 들어 있는 것 (`math`, `random`, `datetime`, `csv`, `json`…)
- **외부 라이브러리**: 따로 설치 (`pip install requests`) — 8장
  - 예: `requests`(인터넷에서 데이터 가져오기), `pandas`(표 데이터 분석), `matplotlib`(그래프)

---

## 7. 종합 예제: 가계부 프로그램

```python
import csv

def add_record(filename, item, amount):
    with open(filename, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow([item, amount])

def summary(filename):
    total = 0
    with open(filename, encoding="utf-8") as f:
        for item, amount in csv.reader(f):
            total += int(amount)
            print(f"{item:<8} {int(amount):>8,}원")
    print(f"{'합계':<8} {total:>8,}원")

add_record("budget.csv", "점심", 9000)
add_record("budget.csv", "커피", 4500)
add_record("budget.csv", "책", 18000)
summary("budget.csv")
```
리스트·문자열·파일·함수가 다 들어 있어요. 여기까지 하면 **기초 2단계 완료**!

---

### 이 장 요약
1. **리스트**는 번호(0부터)로, **딕셔너리**는 이름(키)으로 찾는다. 섞으면 실제 데이터 모양(JSON).
2. 파일은 `with open(...)`, 한글은 `encoding="utf-8"`, `"w"`는 덮어쓰기 주의.
3. 오류 메시지는 **맨 아래 줄부터** 읽고, 예상되는 오류는 `try/except`로 처리한다.
