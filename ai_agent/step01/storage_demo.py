# step01/storage_demo.py
from app.storage import save_conversation, load_conversation

conversation = load_conversation("user01")
print("불러온 메시지 수:", len(conversation))

conversation.append({"role": "user", "content": "연차는 며칠이야?"})
conversation.append({"role": "assistant", "content": "입사 1년 이상이면 연 15일이다."})
save_conversation("user01", conversation)
print("저장한 메시지 수:", len(conversation))