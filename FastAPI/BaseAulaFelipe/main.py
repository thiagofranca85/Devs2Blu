from fastapi import FastAPI

from core.configs import settings

from api.V1.api import api_router


app = FastAPI(

    title = 'MoreDevs',
    version ='007',
    description ='Desenvolvido Python'
    
)

app.include_router(api_router,prefix=settings.API_STR)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run (   
        "main:app",
        host= "127.0.0.1",
        port= 8000,
        log_level= 'info',
        reload = True
    )

