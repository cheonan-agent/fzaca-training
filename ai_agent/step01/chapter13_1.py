from pydantic import ValidationError
from app.models import Message, ChatRequest, ChatResponse, ConversationData

print(Message(role="user", content="    연차는 며칠이야?    "))

for bad in [
    {'role': 'user', 'content': '   '},
    {'role': 'user', 'content': ''},
    {'role': 'user', 'content': '가' * 2001},
]:
    try:
        Message(**bad)
    except ValidationError as e:
        err = e.errors()[0]
        print(err["type"], "|", err["msg"])

req = ChatRequest(session_id="user01", message="출장비 한도는?")
print(req)

res = ChatResponse(session_id=req.session_id, reply="식비 30,000원, 숙박비 100,000원이다.", turns=1)
print(res.model_dump_json())

text = '{"session_id": "user02", "message": "보안 규정 알려줘"}'
req2 = ChatRequest.model_validate_json(text)
print(req2.message)




data = {
    "session_id": "user01",
    "messages": [
        {"role": "user", "content": "연차는 며칠이야?"},
        {"role": "assistant", "content": "입사 1년 이상이면 연 15일이다."}
    ],
}
conv = ConversationData.model_validate(data)
print(type(conv.messages[0]))
print(conv.messages[-1].content)
print(len(conv.messages))

bad = {"sesseion_id": "user01", "messages": [
    {"role": "user", "content": "안녕"},
    {"role": "bot", "content": "안녕"},
]}
try:
    ConversationData.model_validate(bad)
except ValidationError as e:
    print(e.errors()[0]["loc"], e.errors()[0]["msg"])

print("-"*50)
print([m.model_dump() for m in conv.messages])