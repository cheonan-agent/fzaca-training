# step01/chat_utils.py
from datetime import datetime


ALLOWED_ROLES = {"system", "user", "assistant"}


def make_message(role, content):
    return {
        "role": role, 
        "content": content, 
        "time": datetime.now().strftime("%H:%M"),
        }


def add_message(conversation, role, content):
    conversation.append(make_message(role, content))


def format_history(conversation, show_system=False):
    lines = []
    for m in conversation:
        if m["role"] == "system" and not show_system:
            continue
        lines.append(f"[{m['role']}] {m['content']}")
    return "\n".join(lines)

# 기본
ALLOWED_ROLES = {"system", "user", "assistant"}

def is_valid_message(message):
    content = message.get("content")
    return message.get("role") in ALLOWED_ROLES and isinstance(content, str) and bool(content.strip())

# 확장
def trim_history(conversation, max_messages=2):
    system = [m for m in conversation if m["role"] == "system"]
    others = [m for m in conversation if m["role"] != "system"]
    return system + others[-max_messages:]


if __name__ == "__main__":
    test = []
    add_message(test, "user", "테스트 메시지")
    print(format_history(test))