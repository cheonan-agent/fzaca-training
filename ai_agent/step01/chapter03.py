role = "user" # 대입 연산자
content = "연차는 며칠이야?"

print(role)
print(content)
print(id(role)) # 메모리 주소
print(id(content))



model = "gpt-6-luna"      # str   문자열
max_tokens = 500           # int   정수
temperature = 0.7          # float 실수
stream = False             # bool  참/거짓
reply = None               # None  값 없음

print(type(model))
print(type(max_tokens))
print(type(temperature))
print(type(stream))
print(type(reply))

class Member:
    pass
m = Member()
print(type(m))

