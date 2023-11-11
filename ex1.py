from fastapi import APIRouter
from typing import Optional

router = APIRouter()

@router.get("/quadrados")
def quadrados(max: Optional[int] = 10):
    return {
        "max": max,
        "quadrados": [x ** 2 for x in range(max)]
    }