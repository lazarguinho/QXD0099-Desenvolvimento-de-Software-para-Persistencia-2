from fastapi_crudrouter import SQLAlchemyCRUDRouter
from src.models.Categoria import Categoria, CategoriaSchema

from data.database import get_db

categoria_router = SQLAlchemyCRUDRouter(
    schema=CategoriaSchema,
    db_model=Categoria,  
    db=get_db,  
    prefix="categorias", 
    tags=["Categorias"]
)