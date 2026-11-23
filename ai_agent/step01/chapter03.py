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

user_input = "15"

print(user_input + "1")       # 문자열 + 문자열 = 이어 붙이기
print(int(user_input) + 1)    # 정수 + 정수 = 덧셈
print(str(15) + "일")         # 정수를 문자열로
print(float("0.7"))           # 문자열을 실수로

total_days = 38
print(total_days // 7, total_days % 7)   # 38일은 몇 주 며칠?
print(10 / 4, 10 // 4, 2 ** 10)

input_tokens = 1200     # 보낸 토큰
output_tokens = 350     # 받은 토큰
price_per_1k = 0.6      # 1,000 토큰당 가격 (가상)

cost = (input_tokens + output_tokens) / 1000 * price_per_1k
print(cost)
print(round(cost, 4))

role = "user"
years = 2
is_admin = False

print(years >= 1)
print(years == 1)
print(role == "user")
print(years >= 1 and not is_admin)
print(role == "user" or role == "assistant")

count = 0
count += 1      # count = count + 1 과 같다
count += 1
print(count)

def test():
    print("test() func called")
    return True

print(2 > 1 and test())