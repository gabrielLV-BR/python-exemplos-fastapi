from fastapi import APIRouter
from typing import Optional

router = APIRouter()

@router.get("/tabuada/{num}")
def tabuada(num: int, start: Optional[int] = 1, end: Optional[int] = 10):
    return {
        "num": num,
        "start": start,
        "end": end,
        "tabuada": [num * x for x in range(start, end + 1)]
    }