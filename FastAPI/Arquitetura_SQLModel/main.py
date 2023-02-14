from fastapi import FastAPI

from core.configs import settings

from api.v1.api import api_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="API MOREDEVS SQLMODEL")
app.include_router(api_router, prefix=settings.API_STR)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        port=8000, 
        log_level='info', 
        reload=True
        )