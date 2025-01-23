from fastapi_crudrouter import SQLAlchemyCRUDRouter
from src.models.Pedido import Pedido, PedidoCreate, PedidoModel

from data.database import get_db

pedido_router = SQLAlchemyCRUDRouter(
    schema=Pedido,
    create_schema=PedidoCreate,
    db_model=PedidoModel,
    db=get_db,  # Sessão do BD
    prefix="pedidos",
)