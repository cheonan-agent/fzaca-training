# join_months = 8
# leave_days = join_months // 12 * 15 + (join_months % 12) * 1
# print(leave_days)   


# meal_price = 30000
# hotel_price = 100000

# total_visit_price = (meal_price * 3) + (hotel_price * 2)
# print(total_visit_price)

input_price = 0.15 / 1000   # 토큰 1개당 입력 단가
output_price = 0.6 / 1000   # 토큰 1개당 출력 단가

conversations = 10
input_tokens = 800
output_tokens = 300

total_cost = conversations * (input_tokens * input_price + output_tokens * output_price)
print(round(total_cost, 2))

