from fastapi_crudrouter import SQLAlchemyCRUDRouter
from src.models.Pagamento import Pagamento, PagamentoModel, PagamentoCreate

from data.database import get_db

pagamento_CrudRouter = SQLAlchemyCRUDRouter(
    schema=Pagamento,  # Modelo
    create_schema=PagamentoCreate,
    db_model=PagamentoModel,  # Tabela no BD
    db=get_db,  # Sessão do BD
    prefix='pagamentos'
)