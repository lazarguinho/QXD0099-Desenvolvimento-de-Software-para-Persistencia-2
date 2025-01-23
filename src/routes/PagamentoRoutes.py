from fastapi_crudrouter import SQLAlchemyCRUDRouter
from src.models.Pagamento import Pagamento, PagamentoModel, PagamentoCreate

from data.database import get_db

pagamento_CrudRouter = SQLAlchemyCRUDRouter(
    schema=Pagamento,
    create_schema=PagamentoCreate,
    db_model=PagamentoModel,
    db=get_db, 
    prefix='pagamentos'
)