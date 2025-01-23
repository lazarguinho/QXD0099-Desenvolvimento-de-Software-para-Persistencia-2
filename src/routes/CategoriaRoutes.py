from fastapi_crudrouter import SQLAlchemyCRUDRouter
from src.models.Categoria import Categoria, CategoriaCreate, CategoriaModel

from data.database import get_db

categoria_router = SQLAlchemyCRUDRouter(
    schema=Categoria,
    create_schema=CategoriaCreate,
    db_model=CategoriaModel,  
    db=get_db,
    prefix="categorias",
)