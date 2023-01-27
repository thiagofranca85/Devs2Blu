from fastapi import FastAPI, Request

app = FastAPI()

@app.get('/')
async def raiz():
    return {"mensagem": "Seja Bem Vindo ao More Devs"}

alunos = {
    1: "Lirinha",
    2: "Thiago",
    3: "Joao",
    4: "Vander"
}

@app.get('/alunos')
async def get_alunos():
    return alunos

@app.get("/alunos/{aluno_id}/")
async def pegaAlunoId(aluno_id:int):
    return alunos[aluno_id]


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port= 8000,
        log_level = "info",
        reload = True
    )