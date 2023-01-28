from fastapi import FastAPI, HTTPException, status
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

# @app.get("/alunos/{aluno_id}")
# async def get_aluno(aluno_id:int):
#     try:
#         aluno = alunos[aluno_id]
#         return aluno
#     except KeyError:
#         raise HTTPException (
#             status_code = status.HTTP_404_NOT_FOUND, detail='Aluno nao encontrado.' 
#         )

@app.get("/alunos/{aluno_id}")
async def update(aluno_id:int):
    try:
        aluno = alunos[aluno_id]
        alunos.update({"id":aluno_id})
        return aluno
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Aluno nao encontrado."
        )

@app.post("/alunos", status_code=status.HTTP_201_CREATED)
async def post_aluno(aluno:Aluno):
    next_id : int = len(alunos) +1
    alunos[next_id] = aluno
    return aluno

@app.get("/alunosnomes/{aluno_nome}")
async def get_Nomealuno(aluno_nome:str):
    for aluno in alunos.values():
        if aluno['Nome'] == aluno_nome:
            print(aluno['Nome'])
            return aluno




if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port= 8000,
        log_level = "info",
        reload = True
    )