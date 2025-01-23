from fastapi_crudrouter import SQLAlchemyCRUDRouter
from src.models.Pedido import Pedido, PedidoSchema

from data.database import get_db

pedido_router = SQLAlchemyCRUDRouter(
    schema=PedidoSchema,  # Modelo
    db_model=Pedido,  # Tabela no BD
    db=get_db,  # Sessão do BD
    prefix="pedidos",  # Prefixo das rotas
    tags=["Pedidos"]
)