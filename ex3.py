import math
from fastapi import APIRouter
from dataclasses import dataclass

router = APIRouter()

@dataclass
class Equation:
    a: float
    b: float
    c: float

    def __str__(self) -> str:
        a, b, c = self.a, self.b, self.c
        return f"{a:+}x² {b:+}x {c:+}"

class Solution:
    def __init__(self, eq: Equation):
        self.eq = str(eq)
        self.x1, self.x2 = Solution.calculate(eq)

    def calculate(eq: Equation) -> tuple[float, float]:
        a, b, c = eq.a, eq.b, eq.c
        delta = (b ** 2) - (4 * a * c)

        x1 = (- b + math.sqrt(delta)) / (2 * a)
        x2 = (- b - math.sqrt(delta)) / (2 * a)

        return x1, x2

@router.post("/bhaskara")
def bhaskara(equation: Equation):
    return Solution(equation)