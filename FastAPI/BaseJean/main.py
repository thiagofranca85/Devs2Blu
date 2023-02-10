from fastapi import FastAPI
from routes import router_aluno

app = FastAPI(

    title = 'MoreDevs',
    version ='007',
    description ='Desenvolvido Python'
)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run (
        "main:app",
        host= "127.0.0.1",  
        port= 8000,
        log_level= 'info',
        reload = True
    )

