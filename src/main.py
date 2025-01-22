from fastapi import FastAPI
from .routes.UsuarioRoutes import usuario_router
from data.database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(usuario_router)

@app.get('/')
def read_root():
    return { "message": "Bem vindo"}