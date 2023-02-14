from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from models.professor_model import ProfessorModel
from core.dep import get_session

from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True
Select.inherit_cache = True

router = APIRouter()

@router.get('/', response_model=List[ProfessorModel])
async def get_professores(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProfessorModel)

        result= await session.execute(query)

        professores: List[ProfessorModel]= result.scalars().all()

        return professores

@router.get('/{professor_id}', status_code=status.HTTP_200_OK, response_model=ProfessorModel)
async def get_professor(professor_id : int , db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProfessorModel).filter(ProfessorModel.id == professor_id)
        result= await session.execute(query)
        professor : ProfessorModel = result.scalar_one_or_none()

        if professor:
            return professor
        else:
            raise HTTPException(detail='Professor nao encontrado', status_code=status.HTTP_404_NOT_FOUND)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ProfessorModel)
async def post_professor(professor: ProfessorModel, db : AsyncSession = Depends(get_session)):

    novo_professor = ProfessorModel(nome= professor.nome, idade= professor.idade, email=professor.email)

    db.add(novo_professor)
    await db.commit()

    return novo_professor






@router.put('/{professor_id}', status_code=status.HTTP_202_ACCEPTED, response_model=ProfessorModel)
async def put_professor(professor_id : int, professor: ProfessorModel , db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProfessorModel).filter(ProfessorModel.id == professor_id)

        result= await session.execute(query)

        professor_up : ProfessorModel = result.scalar_one_or_none()

        if professor_up:
            professor_up.nome = professor.nome
            professor_up.idade = professor.idade
            professor_up.email = professor.email

            await session.commit()

            return professor_up
        else:
            raise HTTPException(detail='Professor nao encontrado', status_code=status.HTTP_404_NOT_FOUND)
        
@router.delete('/{professor_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_professor(professor_id : int , db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProfessorModel).filter(ProfessorModel.id == professor_id)

        result= await session.execute(query)

        professor_del : ProfessorModel = result.scalar_one_or_none()

        if professor_del:
            await session.delete(professor_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        
        else:
            raise HTTPException(detail='Professor nao encontrado', status_code=status.HTTP_404_NOT_FOUND)