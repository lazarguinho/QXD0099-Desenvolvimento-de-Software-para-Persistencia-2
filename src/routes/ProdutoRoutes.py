from fastapi_crudrouter import SQLAlchemyCRUDRouter
from src.models.Produto import Produto, ProdutoCreate, ProdutoModel

from data.database import get_db    

produto_CrudRouter = SQLAlchemyCRUDRouter(
    schema=Produto,
    create_schema=ProdutoCreate,
    db_model=ProdutoModel,
    db=get_db,  # Sessão do BD
    prefix="produtos",
)