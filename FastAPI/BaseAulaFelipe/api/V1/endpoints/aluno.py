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
from schemas.aluno_schemas import AlunoSchema
from core.deps import get_session

router = APIRouter()


@router.get('/', response_model=List[AlunoSchema])
async def get_alunos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AlunoModel)
        result = await session.execute(query)
        alunos : List[AlunoModel] = result.scalars().all()
        print(alunos)

        return JSONResponse(content=jsonable_encoder(alunos))
    

@router.get('/{alunoID}',response_model=AlunoSchema, status_code=status.HTTP_200_OK)
async def get_aluno(alunoID: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AlunoModel).filter(AlunoModel.id == alunoID)
        result = await session.execute(query)
        aluno = result.scalar_one_or_none()
        if aluno:
            return JSONResponse(content=jsonable_encoder(aluno))
        else:
            raise HTTPException(detail=f'Aluno com o ID {alunoID} Não Encontrado', status_code=status.HTTP_404_NOT_FOUND)



@router.post('/', status_code=status.HTTP_201_CREATED, response_model=str)
async def post_aluno(aluno : AlunoSchema, db: AsyncSession = Depends(get_session)):
    novo_aluno = AlunoModel(nome= aluno.nome, email= aluno.email)
    db.add(novo_aluno)
    await db.commit()
    return JSONResponse(content=jsonable_encoder(novo_aluno))


@router.put('/{alunoID}', response_model=AlunoSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_aluno(alunoID: int, aluno : AlunoSchema, db: AsyncSession = Depends(get_session)):
    async with db as sesssion:
        query = select(AlunoModel).filter(AlunoModel.id == alunoID)
        result = await sesssion.execute(query)
        aluno_up = result.scalar_one_or_none()

        if aluno_up:
            aluno_up.nome = aluno.nome
            aluno_up.email = aluno.email
            await sesssion.commit()
            return JSONResponse(content=jsonable_encoder(aluno_up))
        else:
            raise HTTPException(detail=f'Aluno com o ID {alunoID} Não Encontrado', status_code=status.HTTP_404_NOT_FOUND)


@router.delete('/{alunoID}', response_model=str, status_code=status.HTTP_202_ACCEPTED)
async def delete_aluno(alunoID: int, db: AsyncSession = Depends(get_session)):
    async with db as sesssion:
        query = select(AlunoModel).filter(AlunoModel.id == alunoID)
        result = await sesssion.execute(query)
        aluno_del = result.scalar_one_or_none()

        if aluno_del:
            await sesssion.delete(aluno_del)
            await sesssion.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail=f'Aluno com o ID {alunoID} Não Encontrado', status_code=status.HTTP_404_NOT_FOUND)