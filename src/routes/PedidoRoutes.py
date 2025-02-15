from fastapi_crudrouter import SQLAlchemyCRUDRouter
from src.models.Pedido import Pedido, PedidoCreate, PedidoModel

from data.database import get_db

pedido_CrudRouter = SQLAlchemyCRUDRouter(
    schema=Pedido,
    create_schema=PedidoCreate,
    db_model=PedidoModel,
    db=get_db,
    prefix="pedidos",
)