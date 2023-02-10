from typing import Optional
from sqlmodel import SQLModel, Field
from pydantic import validator

class Aluno(SQLModel, table= True):
    __tablename__ : str = 'Alunos'

    id : Optional[int] = Field(default=None, primary_key=True)
    nome : str
    idade : int
    email : str

    # @validator('nome')
    # def validar_nome(cls, value):
    #     aluno = value.split(' ')
    #     if len(aluno) < 3:
    #         raise ValueError('Nome deve conter no minimo 3 espaco')
    #     return value