from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from models.aluno_model import AlunoModel
from core.dep import get_session

from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True
Select.inherit_cache = True

router = APIRouter()

@router.get('/', response_model=List[AlunoModel])
async def get_alunos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AlunoModel)

        result= await session.execute(query)

        alunos: List[AlunoModel]= result.scalars().all()

        return alunos

@router.get('/{aluno_id}', status_code=status.HTTP_200_OK, response_model=AlunoModel)
async def get_aluno(aluno_id : int , db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AlunoModel).filter(AlunoModel.id == aluno_id)
        result= await session.execute(query)
        aluno : AlunoModel = result.scalar_one_or_none()

        if aluno:
            return aluno
        else:
            raise HTTPException(detail='Aluno nao encontrado', status_code=status.HTTP_404_NOT_FOUND)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=AlunoModel)
async def post_aluno(aluno: AlunoModel, db : AsyncSession = Depends(get_session)):

    novo_aluno = AlunoModel(nome= aluno.nome, idade= aluno.idade, email=aluno.email)

    db.add(novo_aluno)
    await db.commit()

    return novo_aluno






@router.put('/{aluno_id}', status_code=status.HTTP_202_ACCEPTED, response_model=AlunoModel)
async def put_aluno(aluno_id : int, aluno: AlunoModel , db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AlunoModel).filter(AlunoModel.id == aluno_id)

        result= await session.execute(query)

        aluno_up : AlunoModel = result.scalar_one_or_none()

        if aluno_up:
            aluno_up.nome = aluno.nome
            aluno_up.idade = aluno.idade
            aluno_up.email = aluno.email

            await session.commit()

            return aluno_up
        else:
            raise HTTPException(detail='Aluno nao encontrado', status_code=status.HTTP_404_NOT_FOUND)
        
@router.delete('/{aluno_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_aluno(aluno_id : int , db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AlunoModel).filter(AlunoModel.id == aluno_id)

        result= await session.execute(query)

        aluno_del : AlunoModel = result.scalar_one_or_none()

        if aluno_del:
            await session.delete(aluno_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        
        else:
            raise HTTPException(detail='Aluno nao encontrado', status_code=status.HTTP_404_NOT_FOUND)