# app/models.py
from typing import Literal

from pydantic import BaseModel, Field, field_validator

Role = Literal["system", "user", "assistant"]


class Message(BaseModel):
    role: Role
    content: str = Field(min_length=1, max_length=2000)

    @field_validator("content")
    @classmethod
    def strip_content(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("내용이 비어 있다")
        return value


SESSION_ID_PATTERN = r"^[A-Za-z0-9_-]{1,64}$"  # 영문·숫자·_·-만, 64자까지 (파일 이름으로 쓰기 때문)


class ChatRequest(BaseModel):
    session_id: str = Field(pattern=SESSION_ID_PATTERN, examples=["user01"])
    message: str = Field(min_length=1, max_length=2000, examples=["연차는 며칠이야?"])


class ChatResponse(BaseModel):
    session_id: str
    reply: str
    turns: int


class ConversationData(BaseModel):
    session_id: str
    messages: list[Message] = []