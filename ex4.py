from fastapi import APIRouter
from dataclasses import dataclass

router = APIRouter()

@dataclass
class Frase:
    frase: str

def get_count(frase: str) -> tuple[int, int, int]:
    vogais = espacos = outros = 0

    for letra in frase:
        if letra == " ":
            espacos += 1
        elif letra in "aeiou":
            vogais += 1
        else:
            outros += 1

    return vogais, espacos, outros

@router.post("/conta")
def conta(frase: Frase):
    vogais, espacos, outros = get_count(frase.frase)
    return {
        "frase": frase.frase,
        "vogais": vogais,
        "espacos": espacos,
        "outros": outros
    }