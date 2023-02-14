from fastapi import APIRouter

from api.v1.endpoints import aluno
from api.v1.endpoints import usuario
from api.v1.endpoints import professor

api_router = APIRouter()

#/api/v1/alunos
api_router.include_router(aluno.router, prefix='/alunos', tags=["alunos"])
api_router.include_router(usuario.router, prefix='/usuarios', tags=["usuarios"])
api_router.include_router(professor.router, prefix='/professores', tags=["professores"])