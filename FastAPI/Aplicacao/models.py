from typing import Optional
from pydantic import BaseModel

class Aluno(BaseModel):
    id : Optional[int] = None
    nome : str
    idade : int
    email : str
