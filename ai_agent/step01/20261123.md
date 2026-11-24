# 2026-11-23

[ ] 대괄호는 : 복수, 배열 같은 것

### 도전 — pyproject.toml과 uv.lock만 복사해 와서 uv sync로 같은 환경을 만들어 본다.

```
# pyproject.toml
[project]
name = "test"  # <- 프로젝트 디렉토리 name
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "pydantic>=2.14.4",
    "requests>=2.34.2",
]
```

**pyproject.toml**의 
**name** 항목만 새로 복사한 폴더 경로 이름으로 바꾸고 **uv sync**하면 sync가 잘 된다

## chapter03

### 변수 變數(변할 변, 셈 수)

명사
1.	어떤 상황의 가변적 요인.
2.	**수학** 어떤 관계나 범위 안에서 여러 가지 값으로 변할 수 있는 수.

### 변수 이름 
의미가 있는 이름으로 지어야 한다~

| 규칙 | 좋은 예 | 안 되는 예 |
| --- | --- | --- |
| 의미가 드러나는 이름 | `reply`, `leave_days` | `a`, `tmp2` |

#### snakecase, camelcase

- 가독성

snake : 뱀, 회원명 membername -> member_name 

camel : 낙타, 회원명 -> memberName

### 자료형

자료 : data -> 값

형 : type -> 종류

### 기본자료형(primitive type)

중첩 + 양 + 흐름 + 구조

### 주석 (comment)

VS Code 단축키
선택 후 Ctrl + / 하면 전체 주석 혹은 해제

### 파이썬 세미콜론 써도 되는지 처음 알았음

```python
print("hello")print("world")
```
에러

```python
print("hello");print("world")
```
OK

```python
# 01_intro.py
def greet(name: str) -> str:
    return f"Hello, {name}"

def add(a: int, b: int) -> int:
    return a + b


print(greet(3))
print(add("Hello", "Alice"))
```

```bash
Hello, 3
HelloAlice
```

힌트를 줘도 IDE에서 경고는 하지만 실행은 된다.

# 실습 

**기본** — 규정 제2조에 따르면 입사 1년 미만 직원은 매월 1일의 연차가 생긴다. `join_months = 8`일 때 발생한 연차 일수를 변수 `leave_days`에 담아 출력한다.

```python

```

**확장** — 출장 규정(식비 30,000원, 숙박비 100,000원)으로 2박 3일 출장의 최대 출장비를 계산한다. (식비는 3일, 숙박비는 2박)

```python
meal_price = 30000
hotel_price = 100000

total_visit_price = (meal_price * 3) + (hotel_price * 2)
print(total_visit_price)
```

**도전** — 대화 10번에 매번 입력 800 토큰, 출력 300 토큰을 썼다. 입력 단가는 1,000 토큰당 0.15, 출력 단가는 0.6일 때 총비용을 `round()`로 소수점 둘째 자리까지 반올림해 출력한다.

```
input_price = 0.15 / 1000   # 토큰 1개당 입력 단가
output_price = 0.6 / 1000   # 토큰 1개당 출력 단가

conversations = 10
input_tokens = 800
output_tokens = 300

total_cost = conversations * (input_tokens * input_price + output_tokens * output_price)
print(round(total_cost, 2))
```