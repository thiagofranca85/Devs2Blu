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
from schemas.professor_schema import ProfessorSchema
from core.deps import get_session

router = APIRouter()

# Listando todos professores
@router.get('/',response_model=List[ProfessorSchema])
async def get_professores(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProfessorModel)
        result = await session.execute(query)
        professores : List[ProfessorModel] = result.scalars().all()

        return JSONResponse(content=jsonable_encoder(professores))

# Listando Professor
@router.get('/{professor_id}', response_model=ProfessorSchema, status_code=status.HTTP_200_OK)
async def get_professor(professor_id:int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProfessorModel).filter(ProfessorModel.id == professor_id)
        result = await session.execute(query)
        professor = result.scalar_one_or_none()
        if professor:
            return JSONResponse(content=jsonable_encoder(professor))
        else:
            HTTPException(detail='Professor nao encontrado', status_code=status.HTTP_404_NOT_FOUND)

# Criando Professor
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ProfessorSchema)
async def post_professor(professor:ProfessorSchema, db:AsyncSession = Depends(get_session)):
    novo_professor = ProfessorModel(nome = professor.nome, email = professor.email)
    db.add(novo_professor)
    await db.commit()
    return JSONResponse(content=jsonable_encoder(novo_professor))

# Alterar Professor
@router.put('/{professor_id}', response_model=ProfessorSchema, status_code= status.HTTP_202_ACCEPTED)
async def put_professor(professor_id: int, professor: ProfessorSchema, db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProfessorModel).filter(ProfessorModel.id == professor_id)
        result = await session.execute(query)
        professor_up = result.scalar_one_or_none()
        if professor_up:
            professor_up.nome = professor.nome
            professor_up.email = professor.email
            await session.commit()
            return JSONResponse(content=jsonable_encoder(professor_up))
        else:
            raise HTTPException(detail='Professor nao encontrado', status_code=status.HTTP_404_NOT_FOUND)

# Deletar Professor
@router.delete('/{professor_id}', response_model=ProfessorSchema, status_code= status.HTTP_202_ACCEPTED)
async def delete_professor(professor_id: int, db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProfessorModel).filter(ProfessorModel.id == professor_id)
        result = await session.execute(query)
        professor_del = result.scalar_one_or_none()
        if professor_del:
            await session.delete(professor_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Professor nao encontrado', status_code=status.HTTP_404_NOT_FOUND)

