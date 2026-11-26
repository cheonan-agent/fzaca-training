# step01/chapter11.py
from typing import Literal

Role = Literal["system", "user", "assistant"]
Message = dict[str, str]
Conversation = list[Message]


def make_message(role: Role, content: str) -> Message:
    return {"role": role, "content": content}


def last_messages(conversation: Conversation, n: int = 2) -> Conversation:
    return conversation[-n:]


def count_by_role(conversation: Conversation) -> dict[str, int]:
    counts: dict[str, int] = {}
    for m in conversation:
        counts[m["role"]] = counts.get(m["role"], 0) + 1
    return counts


def find_message(conversation: Conversation, keyword: str) -> Message | None:
    for m in conversation:
        if keyword in m["content"]:
            return m
    return None


conversation: Conversation = [
    make_message("user", "연차는 며칠이야?"),
    make_message("assistant", "입사 1년 이상이면 연 15일이다."),
]
print(last_messages(conversation, 1))
print(count_by_role(conversation))
print(find_message(conversation, "15일"))
print(find_message(conversation, "출장"))