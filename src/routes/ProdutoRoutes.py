from fastapi_crudrouter import SQLAlchemyCRUDRouter
from src.models.Produto import Produto, ProdutoSchema

from data.database import get_db    

produto_router = SQLAlchemyCRUDRouter(
    schema=ProdutoSchema,  # Modelo
    db_model=Produto,  # Tabela no BD
    db=get_db,  # Sessão do BD
    prefix="produtos",  # Prefixo das rotas
    tags=["Produtos"]
)