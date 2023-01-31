from fastapi import FastAPI
from fastapi import HTTPException, status, Path
from models import Aluno

app = FastAPI()

@app.get('/')
async def raiz():
    return {"mensagem": "Seja Bem Vindo ao More Devs"}


alunos = {
    1: {"Nome":"Lirinha", "Idade":19, "E-mail":"Lira@mail.com"},
    2: {"Nome":"Thiago", "Idade":37, "E-mail":"thiago@mail.com"},
    3: {"Nome":"Joao", "Idade":17, "E-mail":"joao@mail.com"},
    4: {"Nome":"Vander", "Idade":41, "E-mail":"Lira@mail.com"},

}

@app.get('/alunos')
async def get_alunos():
    return alunos

# Lista o Aluno por ID (Sem salvar o ID consultado)
# @app.get("/alunos/{aluno_id}")
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
@app.get("/alunos/{aluno_id}")
async def mostra_aluno_consultado(aluno_id:int = Path(default=None, title='ID Aluno', description='Deve ser entre 1 e 4', gt=0, lt=5)):
    try:
        aluno = alunos[aluno_id]
        alunos.update({"id":aluno_id})
        return aluno
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Aluno nao encontrado."
        )


# Salvar dados usando POST / Criar novo aluno
@app.post("/alunos", status_code=status.HTTP_201_CREATED)
async def post_aluno(aluno:Aluno):
    next_id : int = len(alunos) +1
    alunos[next_id] = aluno
    del aluno.id
    return aluno

# Buscar aluno pelo nome
@app.get("/alunosnomes/{aluno_nome}")
async def get_Nomealuno(aluno_nome:str):
    for aluno in alunos.values():
        if aluno['Nome'] == aluno_nome:
            print(aluno['Nome'])
            return aluno

# Alterar dados do aluno, consultar o ID do aluno e alterar usando o PUT no Thunder
@app.put("/alunos/{aluno_id}")
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
@app.delete("/alunos/{aluno_id}")
async def delete_aluno(aluno_id: int):
    if aluno_id in alunos:
        del alunos[aluno_id]
        raise HTTPException(status_code=status.HTTP_200_OK, detail="Aluno deletado.")
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Aluno nao encontrado.'
        )

@app.get('/calculadora/')
async def calcular(a: int, b: int, c: int):
    soma = a + b + c
    raise HTTPException(
        status_code=status.HTTP_200_OK, detail=f"NRs - {a} + {b} + {c} = {soma}"
    )

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port= 8000,
        log_level = "info",
        reload = True
    )