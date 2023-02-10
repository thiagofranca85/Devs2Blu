from core.configs import settings
from sqlalchemy import Column, Integer,String


class AlunoModel(settings.DBBaseModel):
    __tablename__ = 'alunos'
    
    id : int = Column(Integer, primary_key=True, autoincrement=True)
    nome : str = Column(String(40))
    email: str = Column(String(40))
