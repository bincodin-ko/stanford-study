# 06. 중급 ①: 객체지향과 코드 정리

프로그램이 수백~수천 줄로 커지면 **"어떻게 나누고 정리하느냐"** 가 실력이 됩니다.
그 대표 방법이 **객체지향 프로그래밍(OOP)** 이에요.

---

## 1. 객체지향이란? — "붕어빵 틀과 붕어빵"

| 용어 | 비유 | 뜻 |
|---|---|---|
| **클래스(Class)** | 붕어빵 **틀** | 어떤 물건의 설계도 |
| **객체(Object) / 인스턴스** | 틀로 찍어 낸 **붕어빵** 하나하나 | 설계도로 만든 실제 물건 |
| **속성(Attribute)** | 붕어빵의 속 재료, 크기 | 객체가 가진 데이터 |
| **메서드(Method)** | "데우기", "포장하기" | 객체가 할 수 있는 행동(함수) |

```python
class Dog:
    def __init__(self, name, age):    # 객체를 만들 때 처음 실행되는 함수(생성자)
        self.name = name              # self = "이 객체 자신"
        self.age = age

    def bark(self):
        print(f"{self.name}: 멍멍!")

    def birthday(self):
        self.age += 1
        print(f"{self.name}는 이제 {self.age}살")

choco = Dog("초코", 3)      # 틀(Dog)로 붕어빵(choco) 만들기
bori = Dog("보리", 5)

choco.bark()               # 초코: 멍멍!
bori.birthday()            # 보리는 이제 6살
```

---

## 2. 객체지향의 4가지 핵심 개념

### ① 캡슐화 — 중요한 건 안에 숨기기
```python
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self._balance = 0            # 밑줄 = "밖에서 직접 건드리지 마세요" 라는 약속

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("입금액은 0보다 커야 합니다")
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("잔액이 부족합니다")
        self._balance -= amount

    def balance(self):
        return self._balance

acc = BankAccount("민수")
acc.deposit(10000)
acc.withdraw(3000)
print(acc.balance())        # 7000
```
잔액을 직접 바꾸지 못하게 하고 **정해진 방법(입금·출금)으로만** 바꾸게 하면, "잔액이 마이너스가 되는" 실수를 막을 수 있어요.

### ② 상속 — 부모 설계도를 물려받기
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("...")

class Cat(Animal):          # Animal을 물려받음
    def speak(self):        # 부모 기능을 내 방식으로 바꿈(오버라이딩)
        print(f"{self.name}: 야옹")

class Cow(Animal):
    def speak(self):
        print(f"{self.name}: 음메")
```

### ③ 다형성 — 같은 명령, 다른 행동
```python
# 위의 Animal, Cat, Cow 코드에 이어서
animals = [Cat("나비"), Cow("누렁이")]
for a in animals:
    a.speak()       # 같은 speak()인데 각자 다르게 동작
# 나비: 야옹
# 누렁이: 음메
```

### ④ 추상화 — 복잡한 속은 감추고 쓰는 법만 보여 주기
자동차 운전자는 엔진 원리를 몰라도 **핸들·페달**만 알면 운전할 수 있죠. 클래스도 **"무엇을 할 수 있는지"** 만 보여 주고 속은 감춥니다.

> ⚠️ 상속은 편하지만 너무 깊게 쓰면(할아버지→아버지→나→자식…) 오히려 복잡해져요. 현업에서는 **"상속보다 조합(composition)"** — 필요한 부품 객체를 안에 넣어 쓰는 방식을 더 자주 권해요.

---

## 3. 프로그래밍 방식(패러다임) 비교

| 방식 | 생각하는 법 | 대표 언어 |
|---|---|---|
| **절차형** | 순서대로 명령을 나열 | C |
| **객체지향** | 데이터와 행동을 묶은 "물건"들이 서로 협력 | 자바, C#, C++ |
| **함수형** | 값을 바꾸지 않고, 입력 → 출력 함수를 조합 | 하스켈, 엘릭서 / JS·파이썬·코틀린도 일부 지원 |

함수형 맛보기:
```python
prices = [3000, 12900, 4500]
with_tax = list(map(lambda p: int(p * 1.1), prices))   # 모든 값에 같은 함수 적용
print(with_tax)          # [3300, 14190, 4950]
```

> 대부분의 현대 언어는 **여러 방식을 섞어서** 써요. "어떤 방식이 정답"이 아니라 상황에 맞게 고르는 게 중급 이상의 실력이에요.

---

## 4. 코드를 파일로 나누기 (모듈)

```
my_shop/
├── main.py          ← 시작점
├── products.py      ← 상품 관련 함수·클래스
├── orders.py        ← 주문 관련
└── utils.py         ← 여기저기서 쓰는 작은 도구
```

```python
# products.py
def format_price(price):
    return f"{price:,}원"
```
```python
# main.py
from products import format_price
print(format_price(12900))     # 12,900원
```

**한 파일 = 한 가지 주제**. 파일 이름만 보고도 어디를 고쳐야 할지 알 수 있게.

---

## 5. 읽기 좋은 코드의 기본 (클린 코드 맛보기)

### 이름이 설명이 되게
```python
# 나쁜 예
def f(a, b):
    return a * b * 0.9

# 좋은 예
DISCOUNT_RATE = 0.9

def discounted_total(unit_price, quantity):
    return unit_price * quantity * DISCOUNT_RATE
```

### 함수는 한 가지 일만
- `처리하기()` 같은 거대한 함수 → `주문_검증()`, `재고_차감()`, `영수증_출력()` 으로 쪼개기
- 함수가 화면 한 페이지를 넘으면 쪼갤 때가 됐다는 신호

### 같은 코드 반복 금지 (DRY: Don't Repeat Yourself)
- 같은 코드를 3번 복사했다면 → 함수로 만들기

### 마법의 숫자 금지
- `if age > 19:` 보다 `ADULT_AGE = 19` 처럼 **이름 붙인 상수**로

### 주석은 "왜"를 쓴다
```python
# 나쁜 주석: i에 1을 더한다
i += 1

# 좋은 주석: 결제 API가 첫 시도에 자주 실패해서 한 번 더 시도한다
retry_count += 1
```

---

### 이 장 요약
1. **클래스** = 설계도(틀), **객체** = 실제 물건(붕어빵). 속성(데이터) + 메서드(행동).
2. 핵심 4가지: **캡슐화·상속·다형성·추상화**. 상속은 적당히, 조합을 더 자주.
3. 코드는 **파일(모듈)로 나누고, 이름으로 설명하고, 함수는 한 가지 일만**.
