# 03. 같은 코드, 다른 언어

똑같은 일을 하는 프로그램을 여러 언어로 써 보면, **언어마다 "말투"만 다르고 생각하는 방식은 거의 같다**는 걸 알 수 있어요.

**만들 프로그램**: 1부터 n까지 더하는 함수 `total`을 만들고, `total(10)`의 결과(55)를 출력하기.

> ✅ 아래 10개 언어 코드는 이 자료를 만들 때 **실제로 실행해서 결과 55가 나오는 것을 확인**했어요.
> (C#·코틀린·스위프트는 실행 환경이 없어 확인하지 못했고, 맨 아래에 참고용으로만 붙였어요.)

---

## 1. 먼저 생각(알고리즘)부터

어떤 언어로 쓰든 생각은 똑같아요.

```
1. 합계 s를 0으로 시작한다
2. i를 1부터 n까지 하나씩 늘리면서
3.     s에 i를 더한다
4. s를 돌려준다
```

이렇게 사람 말로 순서를 적은 것을 **의사코드(pseudo code)** 라고 해요. 고수들도 어려운 문제는 의사코드부터 씁니다.

---

## 2. 10개 언어로 쓴 코드

### 1. 파이썬 (Python)
```python
def total(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

print("합계:", total(10))
```

### 2. C
```c
#include <stdio.h>

int total(int n) {
    int s = 0;
    for (int i = 1; i <= n; i++) {
        s += i;
    }
    return s;
}

int main(void) {
    printf("합계: %d\n", total(10));
    return 0;
}
```

### 3. C++
```cpp
#include <iostream>

int total(int n) {
    int s = 0;
    for (int i = 1; i <= n; i++) {
        s += i;
    }
    return s;
}

int main() {
    std::cout << "합계: " << total(10) << std::endl;
    return 0;
}
```

### 4. 자바 (Java)
```java
public class Main {
    static int total(int n) {
        int s = 0;
        for (int i = 1; i <= n; i++) {
            s += i;
        }
        return s;
    }

    public static void main(String[] args) {
        System.out.println("합계: " + total(10));
    }
}
```

### 5. 자바스크립트 (JavaScript)
```javascript
function total(n) {
  let s = 0;
  for (let i = 1; i <= n; i++) {
    s += i;
  }
  return s;
}

console.log("합계:", total(10));
```

### 6. 타입스크립트 (TypeScript)
```typescript
function total(n: number): number {
  let s = 0;
  for (let i = 1; i <= n; i++) {
    s += i;
  }
  return s;
}

console.log("합계:", total(10));
```

### 7. Go
```go
package main

import "fmt"

func total(n int) int {
	s := 0
	for i := 1; i <= n; i++ {
		s += i
	}
	return s
}

func main() {
	fmt.Println("합계:", total(10))
}
```

### 8. 러스트 (Rust)
```rust
fn total(n: i32) -> i32 {
    let mut s = 0;
    for i in 1..=n {
        s += i;
    }
    s
}

fn main() {
    println!("합계: {}", total(10));
}
```

### 9. PHP
```php
<?php
function total($n) {
    $s = 0;
    for ($i = 1; $i <= $n; $i++) {
        $s += $i;
    }
    return $s;
}

echo "합계: " . total(10) . "\n";
```

### 10. 루비 (Ruby)
```ruby
def total(n)
  s = 0
  (1..n).each do |i|
    s += i
  end
  s
end

puts "합계: #{total(10)}"
```

### 참고: C# / 코틀린 / 스위프트 (실행 확인 못 함)
```csharp
// C#
int Total(int n) {
    int s = 0;
    for (int i = 1; i <= n; i++) {
        s += i;
    }
    return s;
}
Console.WriteLine($"합계: {Total(10)}");
```
```kotlin
// 코틀린
fun total(n: Int): Int {
    var s = 0
    for (i in 1..n) {
        s += i
    }
    return s
}

fun main() {
    println("합계: ${total(10)}")
}
```
```swift
// 스위프트
func total(_ n: Int) -> Int {
    var s = 0
    for i in 1...n {
        s += i
    }
    return s
}
print("합계: \(total(10))")
```

---

## 3. 무엇이 다른가 — 비교표

| 비교 항목 | 파이썬 | C / C++ / 자바 / JS | Go | 러스트 | 루비 |
|---|---|---|---|---|---|
| **코드 묶음 표시** | 들여쓰기(띄어쓰기) | 중괄호 `{ }` | 중괄호 `{ }` | 중괄호 `{ }` | `do ... end` |
| **문장 끝** | 없음 | 세미콜론 `;` | 없음 | 세미콜론 `;` (마지막 값은 생략 가능) | 없음 |
| **함수 만들기** | `def` | `int total(...)` / `function` | `func` | `fn` | `def` |
| **자료형 적기** | 안 적음 (동적) | C·C++·자바는 적음 `int`, JS는 안 적음 | 적음 `int` | 적음 `i32` | 안 적음 |
| **반복 1~n** | `range(1, n + 1)` | `for (i = 1; i <= n; i++)` | `for i := 1; i <= n; i++` | `1..=n` | `(1..n)` |
| **출력** | `print` | `printf` / `cout` / `println` / `console.log` | `fmt.Println` | `println!` | `puts` |
| **실행 방법** | 바로 실행 | C·C++: 컴파일 후 실행 / 자바: 컴파일 후 가상 머신 / JS: 바로 실행 | 컴파일 | 컴파일 | 바로 실행 |

### 알아 두면 좋은 차이
- **파이썬의 `range(1, n + 1)`** 은 1부터 n까지예요. 끝 숫자는 **포함하지 않기** 때문에 `n + 1`까지로 써요. (초보자가 가장 많이 헷갈리는 부분!)
- **C의 `int`** 는 담을 수 있는 숫자 크기에 한계가 있어요(보통 약 21억). 그보다 커지면 엉뚱한 값이 나오는 **오버플로**가 생겨요. 파이썬은 아주 큰 정수도 알아서 처리해요.
- **러스트의 `let mut`**: 러스트는 변수가 기본적으로 **바꿀 수 없고**, 바꿀 변수에는 `mut`(mutable, 바뀔 수 있음)을 붙여야 해요. 실수를 줄이려는 설계예요.
- **PHP의 `$`**: 변수 이름 앞에 항상 `$`를 붙여요.

---

## 4. 직접 해 보기

1. 위 코드 중 하나를 골라 **`total(100)`** 으로 바꿔 보세요. 결과는 5050이 나와야 해요.
2. 1부터 n까지 **짝수만** 더하도록 바꿔 보세요. (힌트: 4장의 조건문 `if i % 2 == 0`)
3. 같은 일을 **반복문 없이** 할 수 있을까요? (힌트: 가우스의 공식 `n × (n + 1) ÷ 2`) → 7장에서 이게 왜 "더 빠른 코드"인지 배워요.

---

### 이 장 요약
1. 언어가 달라도 **생각(알고리즘)은 같고, 말투(문법)만 다르다.**
2. 차이는 주로 **코드 묶음 표시, 자료형 적기, 반복문 모양, 실행 방식**.
3. 어려운 문제는 **의사코드**로 순서부터 적는다.
