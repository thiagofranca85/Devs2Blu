from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.aluno_models import AlunoModel
from schemas.aluno_schema import AlunoSchema
from core.deps import get_session

router = APIRouter()

# Listando todos Alunos
@router.get('/',response_model=List[AlunoSchema])
async def get_alunos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AlunoModel)
        result = await session.execute(query)
        alunos : List[AlunoModel] = result.scalars().all()

        return JSONResponse(content=jsonable_encoder(alunos))

# Listando Aluno
@router.get('/{aluno_id}', response_model=AlunoSchema, status_code=status.HTTP_200_OK)
async def get_aluno(aluno_id:int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AlunoModel).filter(AlunoModel.id == aluno_id)
        result = await session.execute(query)
        aluno = result.scalar_one_or_none()
        if aluno:
            return JSONResponse(content=jsonable_encoder(aluno))
        else:
            HTTPException(detail='Aluno nao encontrado', status_code=status.HTTP_404_NOT_FOUND)

# Criando Aluno
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=AlunoSchema)
async def post_aluno(aluno:AlunoSchema, db:AsyncSession = Depends(get_session)):
    novo_aluno = AlunoModel(nome = aluno.nome, email = aluno.email)
    db.add(novo_aluno)
    await db.commit()
    return JSONResponse(content=jsonable_encoder(novo_aluno))

# Alterar Aluno
@router.put('/{aluno_id}', response_model=AlunoSchema, status_code= status.HTTP_202_ACCEPTED)
async def put_aluno(aluno_id: int, aluno: AlunoSchema, db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AlunoModel).filter(AlunoModel.id == aluno_id)
        result = await session.execute(query)
        aluno_up = result.scalar_one_or_none()
        if aluno_up:
            aluno_up.nome = aluno.nome
            aluno_up.email = aluno.email
            await session.commit()
            return JSONResponse(content=jsonable_encoder(aluno_up))
        else:
            raise HTTPException(detail='Aluno nao encontrado', status_code=status.HTTP_404_NOT_FOUND)

# Deletar Aluno
@router.delete('/{aluno_id}', response_model=AlunoSchema, status_code= status.HTTP_202_ACCEPTED)
async def delete_aluno(aluno_id: int, db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AlunoModel).filter(AlunoModel.id == aluno_id)
        result = await session.execute(query)
        aluno_del = result.scalar_one_or_none()
        if aluno_del:
            await session.delete(aluno_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Aluno nao encontrado', status_code=status.HTTP_404_NOT_FOUND)

