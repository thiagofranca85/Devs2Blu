from sqlmodel import SQLModel, create_engine
from models.aluno import Aluno

engine = create_engine("postgresql://teste2:1234@localhost:5433/postgres")


SQLModel.metadata.create_all(engine)