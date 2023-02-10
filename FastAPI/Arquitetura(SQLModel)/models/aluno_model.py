from typing import Optional
from sqlmodel import Field, SQLModel 

class AlunoModel(SQLModel, table=True):
    __tablename__: str = 'alunos'

    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    idade: int
    email: str
    