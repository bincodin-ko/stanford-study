# 07. 중급 ②: 자료구조와 알고리즘

- **자료구조** = 데이터를 **어떻게 담아 둘까** (서랍장, 줄 서기, 사전, 나무 모양…)
- **알고리즘** = 문제를 **어떤 순서로 풀까** (찾기, 정렬하기, 길 찾기…)

같은 결과를 내도 방법에 따라 **1초 걸리는 코드**와 **1시간 걸리는 코드**가 갈려요. 이걸 구분하는 게 중급 개발자의 핵심 실력이고, 개발자 취업 **코딩 테스트**의 주제이기도 합니다.

---

## 1. 빅오(Big-O) — 코드가 얼마나 빠른지 재는 자

**빅오** = "데이터가 n개로 늘어나면, 일하는 양이 얼마나 늘어나는가?"

| 표기 | 이름 | 비유 | n = 100만일 때 대략 |
|---|---|---|---|
| **O(1)** | 상수 시간 | 사물함 번호로 바로 열기 | 1번 |
| **O(log n)** | 로그 시간 | 사전에서 단어 찾기 (반씩 펼치기) | 약 20번 |
| **O(n)** | 선형 시간 | 줄 선 사람 한 명씩 확인 | 100만 번 |
| **O(n log n)** | | 좋은 정렬 방법 | 약 2,000만 번 |
| **O(n²)** | 제곱 시간 | 반 학생 모두가 서로 한 번씩 악수 | **1조 번** 😱 |
| **O(2ⁿ)** | 지수 시간 | 모든 조합 다 해 보기 | 사실상 끝나지 않음 |

### 예: 3장의 1~n 합계
```python
def total_loop(n):          # O(n): n번 더함
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

def total_formula(n):       # O(1): n이 아무리 커도 계산 한 번
    return n * (n + 1) // 2

print(total_loop(1000000))      # 500000500000
print(total_formula(1000000))   # 500000500000  (같은 결과, 훨씬 빠름)
```

---

## 2. 꼭 알아야 할 자료구조

### ① 배열 / 리스트 — 번호 붙은 칸
- 번호로 꺼내기: **O(1)** (빠름)
- 값으로 찾기: **O(n)** (처음부터 하나씩 확인)
- 중간에 끼워 넣기: **O(n)** (뒤에 있는 것들을 다 밀어야 함)

### ② 스택(Stack) — 접시 쌓기 (나중에 넣은 게 먼저 나옴, LIFO)
```python
stack = []
stack.append("페이지1")
stack.append("페이지2")
stack.append("페이지3")
print(stack.pop())     # 페이지3  ← 브라우저 "뒤로 가기"가 이 원리
```
쓰이는 곳: 뒤로 가기, 실행 취소(Ctrl+Z), 괄호 짝 맞추기, 함수 호출 기록

### ③ 큐(Queue) — 줄 서기 (먼저 온 사람이 먼저, FIFO)
```python
from collections import deque
queue = deque()
queue.append("손님1")
queue.append("손님2")
print(queue.popleft())  # 손님1
```
쓰이는 곳: 주문 처리 대기열, 프린터 대기, 게임 매칭 대기열(사업 20장)

### ④ 해시 테이블 / 딕셔너리 — 이름표로 바로 찾기
- 키로 찾기·넣기·지우기: **평균 O(1)** ← 매우 빠름
- 파이썬 `dict`, 자바 `HashMap`, 자바스크립트 `Map`/객체
```python
# 리스트에서 찾기: O(n)
users_list = ["kim", "lee", "park"]
print("park" in users_list)

# 집합/딕셔너리에서 찾기: 평균 O(1)
users_set = {"kim", "lee", "park"}
print("park" in users_set)
```
> 💡 "데이터가 많은데 자주 찾는다" → **딕셔너리·집합**을 떠올리세요. 실무에서 가장 효과가 큰 최적화 중 하나예요.

### ⑤ 트리(Tree) — 나무 모양 (가계도, 폴더 구조)
```
        회사
       /    \
    개발팀   영업팀
    /   \
  웹팀   앱팀
```
- **이진 탐색 트리**: 왼쪽엔 작은 값, 오른쪽엔 큰 값 → 찾기 평균 O(log n)
- 쓰이는 곳: 폴더 구조, 웹 페이지 구조(HTML DOM), **데이터베이스 인덱스**(9장)

### ⑥ 그래프(Graph) — 점과 선의 연결망
- 지하철 노선도, SNS 친구 관계, 지도 길 찾기
- 대표 알고리즘: **BFS**(가까운 곳부터 퍼지듯 탐색), **DFS**(한 길을 끝까지 갔다가 돌아오기), **다익스트라**(최단 경로)

### 자료구조 고르기 요약
| 이런 일이 많으면 | 이걸 쓴다 |
|---|---|
| 순서대로 모아 두고 번호로 꺼냄 | 리스트(배열) |
| 마지막 것부터 꺼냄 | 스택 |
| 먼저 온 것부터 처리 | 큐 |
| 이름(키)으로 빨리 찾음 | 해시(딕셔너리·집합) |
| 계층 구조 / 정렬된 상태로 빨리 찾음 | 트리 |
| 연결 관계 / 경로 | 그래프 |

---

## 3. 꼭 알아야 할 알고리즘

### ① 탐색 — 찾기
```python
def linear_search(items, target):          # O(n): 처음부터 하나씩
    for i, value in enumerate(items):
        if value == target:
            return i
    return -1

def binary_search(sorted_items, target):   # O(log n): 정렬된 목록을 반씩 잘라가며
    low, high = 0, len(sorted_items) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_items[mid] == target:
            return mid
        elif sorted_items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

nums = [3, 8, 15, 23, 42, 57, 91]
print(linear_search(nums, 42))   # 4
print(binary_search(nums, 42))   # 4
```
> **이진 탐색**은 "업다운 숫자 맞히기"(4장 게임)의 최적 전략이에요. 1~100이면 최대 7번 만에 맞힐 수 있어요.

### ② 정렬 — 순서대로 늘어놓기
| 정렬 | 아이디어 | 속도 |
|---|---|---|
| 버블 정렬 | 옆끼리 비교해서 큰 걸 뒤로 계속 보내기 | O(n²) — 배우기용 |
| 선택 정렬 | 가장 작은 걸 찾아 맨 앞으로 | O(n²) |
| **병합 정렬** | 반으로 쪼개 각각 정렬한 뒤 합치기 | O(n log n) |
| **퀵 정렬** | 기준값보다 작은 쪽/큰 쪽으로 나누기 | 평균 O(n log n) |

```python
def bubble_sort(items):
    arr = items[:]                       # 원본을 건드리지 않게 복사
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]   # 자리 바꾸기
    return arr

def merge_sort(items):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    return merged + left[i:] + right[j:]

data = [5, 2, 9, 1, 7]
print(bubble_sort(data))   # [1, 2, 5, 7, 9]
print(merge_sort(data))    # [1, 2, 5, 7, 9]
print(sorted(data))        # [1, 2, 5, 7, 9]  ← 실무에선 내장 정렬을 쓰세요 (O(n log n))
```

### ③ 재귀 — 자기 자신을 부르는 함수
```python
def factorial(n):
    if n <= 1:          # 멈추는 조건(기저 조건)이 꼭 있어야 함!
        return 1
    return n * factorial(n - 1)

print(factorial(5))     # 120  (5 × 4 × 3 × 2 × 1)
```
> ⚠️ 멈추는 조건이 없으면 끝없이 자기를 불러서 **스택 오버플로**(기록 쌓을 공간이 넘침) 오류가 나요.

### ④ 그 밖에 중요한 알고리즘 아이디어
| 이름 | 아이디어 | 예 |
|---|---|---|
| **동적 계획법(DP)** | 작은 문제의 답을 저장해 두고 재사용 | 피보나치, 최소 동전 개수 |
| **그리디(욕심쟁이)** | 매 순간 가장 좋아 보이는 선택 | 거스름돈 (큰 동전부터) |
| **투 포인터 / 슬라이딩 윈도우** | 두 개의 손가락을 움직이며 범위 탐색 | 연속 구간의 합 |
| **BFS / DFS** | 그래프를 넓게/깊게 탐색 | 미로 찾기 |

### 동적 계획법 맛보기 — 같은 계산 반복하지 않기
```python
from functools import lru_cache

@lru_cache(maxsize=None)     # 계산 결과를 기억해 두는 장치
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(80))    # 23416728348467685  (기억 장치가 없으면 사실상 끝나지 않는 계산)
```

---

## 4. 코딩 테스트 준비 방법

1. **한 언어를 정한다** (파이썬이 문법이 짧아서 많이 씀)
2. 쉬운 문제부터: 백준, 프로그래머스, LeetCode 같은 사이트의 **입문 단계** 문제
3. 유형별로: 구현 → 정렬·탐색 → 스택·큐·해시 → BFS·DFS → DP → 그리디
4. 풀고 나서 **다른 사람 풀이 보기** — 이게 실력이 가장 많이 느는 단계
5. 매일 1~2문제가 한 번에 10문제보다 낫다

---

### 이 장 요약
1. **빅오**로 속도를 잰다: O(1) < O(log n) < O(n) < O(n log n) < O(n²).
2. 자료구조: **리스트·스택·큐·해시·트리·그래프**. 자주 찾으면 해시.
3. 알고리즘: **탐색(이진 탐색)·정렬(병합·퀵)·재귀·DP·그리디·BFS/DFS**.
