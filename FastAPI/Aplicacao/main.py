from fastapi import FastAPI
from fastapi import HTTPException, status
from models import Aluno, alunos
from fastapi import Response, Path, Query, Header, Depends
from typing import Optional, Dict, List, Any
from time import sleep

app = FastAPI(
    title='MoreDevs2Blu',
    version='007',
    description='Desenvolvido pela melhor turma da história',
        contact={
        "name": "Thiago",
        "url": "https://github.com/thiagofranca85",
        "email": "thiagoaugusto.franca@hotmail.com",
    }
)

@app.get('/')
async def root():
    return {"mensagem": "Seja Bem Vindo ao More Devs"}

def db():
    try:
        print('conexao com banco')
        sleep(1)
    finally:
        print('conexao com banco')
        sleep(1)

@app.get('/alunos', 
        description='Lista de todos os Alunos', 
        summary='Lista de todos os Alunos',
        response_description='Retorna os Alunos Cadastrados',
        response_model=List[Aluno]
        )
async def get_alunos():
    return alunos

# Lista o Aluno por ID (Sem salvar o ID consultado)
# @app.get("/alunos/{aluno_id}",
#         description='Consulta aluno por ID',
#         summary='Salva a Ultima Consulta e "Cache"',
#         response_description='Retorna Aluno consultado pelo ID'
#         )
# async def get_aluno(aluno_id:int):
#     try:
#         aluno = alunos[aluno_id]
#         return aluno
#     except KeyError:
#         raise HTTPException (
#             status_code = status.HTTP_404_NOT_FOUND, detail='Aluno nao encontrado.' 
#         )

# Evidencia o ID consultado no final (Cache) - Se a função acima estiver descomentada sobre-escreve essa aqui.
# Ao consulta todos os alunos depois de consultar 1 ID aparece o ID consultado no final (No get)
@app.get("/alunos/{aluno_id}",
        description='Consulta aluno por ID / Salva o Ultimo ID consultado em "Cache"',
        summary='Consulta aluno por ID',
        response_description='Consulta aluno pelo ID e apartir da 2a consulta salva o "Cache"'
        # response_model=List[Aluno]
        )
async def mostra_aluno_consultado(aluno_id: int = Path(default=None, title='ID Aluno', description='Deve ser entre 1 ou 2', gt=0, lt=7), db :Any =Depends(db)):
    try:
        # aluno = alunos[aluno_id]
        # print(alunos)
        for aluno in alunos:
            if aluno.id == aluno_id:
                return aluno


    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Aluno nao encontrado."
        )


# Salvar dados usando POST / Criar novo aluno
@app.post("/alunos", 
        status_code=status.HTTP_201_CREATED,
        description='Salva/Cria uma novo aluno',
        summary='Criar um novo Aluno',
        response_description='Salva o novo aluno Cadastrado'
        )
async def post_aluno(aluno:Aluno):
    next_id : int = len(alunos) +1
    alunos[next_id] = aluno
    del aluno.id
    return aluno

# Buscar aluno pelo nome
@app.get("/alunosnomes/{aluno_nome}",
        description='Buscar aluno pelo nome.',
        summary='Busca aluno pelo nome',
        response_description='Retorna o aluno consultado pelo nome'
        )
async def get_Nomealuno(aluno_nome:str):
    for aluno in alunos.values():
        if aluno['Nome'] == aluno_nome:
            print(aluno['Nome'])
            return aluno

# Alterar dados do aluno, consultar o ID do aluno e alterar usando o PUT no Thunder
@app.put("/alunos/{aluno_id}",
        description='Alterar dados do aluno usando o ID e pegando infos do Body',
        summary='Alterar dados do aluno pelo ID',
        response_description='Retorna aluno com dados alterados'
        )
async def put_aluno(aluno_id: int, aluno:Aluno):
    if aluno_id in alunos:
        alunos[aluno_id] = aluno
        del aluno.id
        return aluno
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Aluno nao encontrado.'
        )

# Deletar o aluno pelo ID
@app.delete("/alunos/{aluno_id}",
        description='Deletar aluno pelo ID',
        summary='Deletar aluno pelo ID',
        response_description='Efetua o delete do aluno pelo ID'
        )
async def delete_aluno(aluno_id: int):
    if aluno_id in alunos:
        del alunos[aluno_id]
        # raise HTTPException(status_code=status.HTTP_200_OK, detail="Aluno deletado.")
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Aluno nao encontrado.'
        )

@app.get('/calculadora/',
        description='Calculadora usando Query, Optional e Header',
        summary='Calculadora',
        response_description='Retorna o resultado e o valor do Header"xdevs" caso tenha.')
async def calcular(a: int = Query(default=None, gt=5), b: int = Query(default=None, gt=5), c: Optional[int] = None, xdevs: str =Header(default=None)):
    soma = a + b
    if c:
        soma = soma + c
    print(f'devs: {xdevs}')
    return soma     


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port= 8000,
        log_level = "info",
        reload = True
    )