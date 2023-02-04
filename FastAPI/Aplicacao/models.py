from typing import Optional
from pydantic import BaseModel, validator

class Aluno(BaseModel):
    id : Optional[int] = None
    nome : str
    idade : int
    email : str

    @validator('nome')
    def validar_nome(cls, value):
        abacate = value.split(' ')
        if len(abacate) < 3:
            raise ValueError('O nome deve ter no minimo 3 espaços')
        return value

alunos = [
    Aluno(id=1, nome="Thiago A França", idade=37, email="Thiago@email.com"),
    Aluno(id=2, nome="Joao de Oliveira", idade=17, email="joao@email.com"),
    Aluno(id=3, nome="Vander Rolly Field", idade=41, email="vander@email.com"),
    Aluno(id=4, nome="Jean Carlos Niehues", idade=42, email="jean@email.com")
]