from fastapi_crudrouter import SQLAlchemyCRUDRouter
from src.models.ItemPedido import ItemPedido, ItemPedidoSchema

from data.database import get_db

item_pedido_router = SQLAlchemyCRUDRouter(
    schema=ItemPedidoSchema,  # Modelo
    db_model=ItemPedido,  # Tabela no BD
    db=get_db,  # Sessão do BD
    prefix="itempedidos",  # Prefixo das rotas
    tags=["ItemPedidos"]
)