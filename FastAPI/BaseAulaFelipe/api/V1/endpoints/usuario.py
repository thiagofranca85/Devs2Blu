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

from models.usuario_models import UsuarioModel
from schemas.usuario_schemas import UsuarioSchema
from core.deps import get_session

router = APIRouter()


@router.get('/', response_model=List[UsuarioSchema])
async def get_usuarios(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel)
        result = await session.execute(query)
        usuarios : List[UsuarioModel] = result.scalars().all()
        print(usuarios)

        return JSONResponse(content=jsonable_encoder(usuarios))
    

@router.get('/{usuarioID}',response_model=UsuarioSchema, status_code=status.HTTP_200_OK)
async def get_usuario(usuarioID: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == usuarioID)
        result = await session.execute(query)
        usuario = result.scalar_one_or_none()
        if usuario:
            return JSONResponse(content=jsonable_encoder(usuario))
        else:
            raise HTTPException(detail=f'Usuario com o ID {usuarioID} Não Encontrado', status_code=status.HTTP_404_NOT_FOUND)



@router.post('/', status_code=status.HTTP_201_CREATED, response_model=str)
async def post_usuario(usuario : UsuarioSchema, db: AsyncSession = Depends(get_session)):
    novo_usuario = UsuarioModel(nome= usuario.nome, email= usuario.email)
    db.add(novo_usuario)
    await db.commit()
    return JSONResponse(content=jsonable_encoder(novo_usuario))


@router.put('/{usuarioID}', response_model=UsuarioSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_usuario(usuarioID: int, usuario : UsuarioSchema, db: AsyncSession = Depends(get_session)):
    async with db as sesssion:
        query = select(UsuarioModel).filter(UsuarioModel.id == usuarioID)
        result = await sesssion.execute(query)
        usuario_up = result.scalar_one_or_none()

        if usuario_up:
            usuario_up.nome = usuario.nome
            usuario_up.email = usuario.email
            await sesssion.commit()
            return JSONResponse(content=jsonable_encoder(usuario_up))
        else:
            raise HTTPException(detail=f'usuario com o ID {usuarioID} Não Encontrado', status_code=status.HTTP_404_NOT_FOUND)


@router.delete('/{usuarioID}', response_model=str, status_code=status.HTTP_202_ACCEPTED)
async def delete_usuario(usuarioID: int, db: AsyncSession = Depends(get_session)):
    async with db as sesssion:
        query = select(UsuarioModel).filter(UsuarioModel.id == usuarioID)
        result = await sesssion.execute(query)
        usuario_del = result.scalar_one_or_none()

        if usuario_del:
            await sesssion.delete(usuario_del)
            await sesssion.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail=f'usuario com o ID {usuarioID} Não Encontrado', status_code=status.HTTP_404_NOT_FOUND)