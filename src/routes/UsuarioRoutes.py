from fastapi_crudrouter import SQLAlchemyCRUDRouter
from src.models.Usuario import Usuario, UsuarioCreate, UsuarioModel
from data.database import get_db


usuario_router = SQLAlchemyCRUDRouter(
    schema=Usuario,  # Modelo
    create_schema=UsuarioCreate,  # Modelo para criação
    db_model=UsuarioModel,  # Tabela no BD
    db=get_db,  # Sessão do BD
    prefix='usuarios'
)