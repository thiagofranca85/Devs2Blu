from fastapi import APIRouter

from api.V1.endpoints import aluno
from api.V1.endpoints import professor
from api.V1.endpoints import usuario

api_router = APIRouter()

api_router.include_router(aluno.router, prefix='/alunos', tags=["Alunos"])
api_router.include_router(professor.router, prefix='/professores', tags=["Professores"])
api_router.include_router(usuario.router, prefix='/usuarios', tags=["Usuarios"])
