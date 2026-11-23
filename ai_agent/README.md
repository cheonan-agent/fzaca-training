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

