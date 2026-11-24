print("앵무새 챗봇입니다. '종료'를 입력하면 끝납니다.")
conversation = []

while True:
    user_input = input("👤 ").strip()

    if user_input == "종료":
        print("대화를 종료합니다.")
        break
    if not user_input:
        continue

    conversation.append({"role": "user", "content": user_input})
    reply = f"'{user_input}'라고 하셨네요."
    conversation.append({"role": "assistant", "content": reply})
    print(f"🤖 {reply}")

print(f"총 메시지 수: {len(conversation)}")