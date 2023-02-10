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

from models.professor_models import ProfessorModel
from schemas.professor_schemas import ProfessorSchema
from core.deps import get_session

router = APIRouter()

@router.get('/', response_model=List[ProfessorSchema])
async def get_professores(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProfessorModel)
        result = await session.execute(query)
        professores : List[ProfessorModel] = result.scalars().all()
        print(professores)

        return JSONResponse(content=jsonable_encoder(professores))
    

@router.get('/{professorID}',response_model=ProfessorSchema, status_code=status.HTTP_200_OK)
async def get_professor(professorID: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProfessorModel).filter(ProfessorModel.id == professorID)
        result = await session.execute(query)
        professor = result.scalar_one_or_none()
        if professor:
            return JSONResponse(content=jsonable_encoder(professor))
        else:
            raise HTTPException(detail=f'professor com o ID {professorID} Não Encontrado', status_code=status.HTTP_404_NOT_FOUND)



@router.post('/', status_code=status.HTTP_201_CREATED, response_model=str)
async def post_professor(professor : ProfessorSchema, db: AsyncSession = Depends(get_session)):
    novo_professor = ProfessorModel(nome= professor.nome, idade= professor.idade)
    db.add(novo_professor)
    await db.commit()
    return JSONResponse(content=jsonable_encoder(novo_professor))


@router.put('/{professorID}', response_model=ProfessorSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_professor(professorID: int, professor : ProfessorSchema, db: AsyncSession = Depends(get_session)):
    async with db as sesssion:
        query = select(ProfessorModel).filter(ProfessorModel.id == professorID)
        result = await sesssion.execute(query)
        professor_up = result.scalar_one_or_none()

        if professor_up:
            professor_up.nome = professor.nome
            professor_up.email = professor.email
            await sesssion.commit()
            return JSONResponse(content=jsonable_encoder(professor_up))
        else:
            raise HTTPException(detail=f'professor com o ID {professorID} Não Encontrado', status_code=status.HTTP_404_NOT_FOUND)

@router.delete('/{professorID}', response_model=str, status_code=status.HTTP_202_ACCEPTED)
async def delete_professor(professorID: int, db: AsyncSession = Depends(get_session)):
    async with db as sesssion:
        query = select(ProfessorModel).filter(ProfessorModel.id == professorID)
        result = await sesssion.execute(query)
        professor_del = result.scalar_one_or_none()

        if professor_del:
            await sesssion.delete(professor_del)
            await sesssion.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail=f'professor com o ID {professorID} Não Encontrado', status_code=status.HTTP_404_NOT_FOUND)