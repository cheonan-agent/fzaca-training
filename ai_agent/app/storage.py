# app/storage.py
import json
from pathlib import Path

DATA_DIR = Path("data") / "conversations"


def _path(session_id):
    return DATA_DIR / f"{session_id}.json"


def save_conversation(session_id: str, conversation: list[dict[str, str]]) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(_path(session_id), "w", encoding="utf-8") as f:
        json.dump(conversation, f, ensure_ascii=False, indent=2)


def load_conversation(session_id: str) -> list[dict[str, str]]:
    path = _path(session_id)
    if not path.exists():
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)