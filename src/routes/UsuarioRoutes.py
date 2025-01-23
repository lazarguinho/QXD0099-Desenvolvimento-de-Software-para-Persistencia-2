from fastapi_crudrouter import SQLAlchemyCRUDRouter
from src.models.Usuario import Usuario, UsuarioCreate, UsuarioModel
from src.services.UsuarioServices import count_usuarios
from data.database import get_db
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import APIRouter

usuario_router = APIRouter()

@usuario_router.get("/get", summary="Retorna a quantidade total de usuários cadastrados")
def get_quantidade_usuarios(db: Session = Depends(get_db)):
    quantidade = db.query(UsuarioModel).count()
    return {"quantidade": quantidade}

usuario_CrudRouter = SQLAlchemyCRUDRouter(
    schema=Usuario,  # Modelo
    create_schema=UsuarioCreate,  # Modelo para criação
    db_model=UsuarioModel,  # Tabela no BD
    db=get_db,  # Sessão do BD
    prefix='usuarios'
)


