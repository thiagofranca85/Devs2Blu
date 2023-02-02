from typing import Optional
from pydantic import BaseModel

class Aluno(BaseModel):
    id : Optional[int] = None
    nome : str
    idade : int
    email : str

alunos = [
    Aluno(id=1, nome="Thiago", idade=37, email="Thiago@email.com"),
    Aluno(id=2, nome="Joao", idade=17, email="joao@email.com"),
    Aluno(id=3, nome="Vander", idade=41, email="vander@email.com"),
    Aluno(id=4, nome="Jean", idade=42, email="jean@email.com")
]