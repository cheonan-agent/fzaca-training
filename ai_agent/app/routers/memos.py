# app/routers/memos.py (1/4)
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field

router = APIRouter(prefix="/memos", tags=["memos"])


class MemoCreate(BaseModel):
    title: str = Field(min_length=1, max_length=50, examples=["출장 보고서"])
    content: str = Field(min_length=1, max_length=1000, examples=["복귀 후 5영업일 이내 제출"])


class Memo(MemoCreate):
    id: int
    created_at: datetime

# app/routers/memos.py (2/4)
class MemoStore:
    def __init__(self):
        self.memos: dict[int, Memo] = {}
        self.next_id = 1

    def add(self, data: MemoCreate) -> Memo:
        memo = Memo(id=self.next_id, created_at=datetime.now(), **data.model_dump())
        self.memos[memo.id] = memo
        self.next_id += 1
        return memo


store = MemoStore()


def get_store() -> MemoStore:
    return store

# app/routers/memos.py (3/4)
@router.post("", response_model=Memo, status_code=status.HTTP_201_CREATED)
def create_memo(data: MemoCreate, store: MemoStore = Depends(get_store)):
    return store.add(data)


@router.get("", response_model=list[Memo])
def list_memos(keyword: str | None = None, store: MemoStore = Depends(get_store)):
    memos = list(store.memos.values())
    if keyword:
        memos = [m for m in memos if keyword in m.title or keyword in m.content]
    return memos


@router.get("/{memo_id}", response_model=Memo)
def get_memo(memo_id: int, store: MemoStore = Depends(get_store)):
    memo = store.memos.get(memo_id)
    if memo is None:
        raise HTTPException(status_code=404, detail=f"{memo_id}번 메모가 없다")
    return memo

# app/routers/memos.py (4/4)
@router.put("/{memo_id}", response_model=Memo)
def update_memo(memo_id: int, data: MemoCreate, store: MemoStore = Depends(get_store)):
    memo = get_memo(memo_id, store)                       # 없으면 여기서 404
    updated = memo.model_copy(update=data.model_dump())
    store.memos[memo_id] = updated
    return updated


@router.delete("/{memo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_memo(memo_id: int, store: MemoStore = Depends(get_store)):
    get_memo(memo_id, store)
    del store.memos[memo_id]

