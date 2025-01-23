from fastapi_crudrouter import SQLAlchemyCRUDRouter
from src.models.Pagamento import Pagamento, PagamentoSchema

from data.database import get_db

pagamento_router = SQLAlchemyCRUDRouter(
    schema=PagamentoSchema,  # Modelo
    db_model=Pagamento,  # Tabela no BD
    db=get_db,  # Sessão do BD
    prefix="pagamentos",  # Prefixo das rotas
    tags=["Pagamentos"]
)