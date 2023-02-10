from typing import Optional
from pydantic import BaseModel as SCBaseModel

class UsuarioSchema(SCBaseModel):
    id : Optional[int]
    nome : str
    email : str

    class config():
        orm_mode = True