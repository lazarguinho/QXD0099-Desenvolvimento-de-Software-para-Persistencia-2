from fastapi_crudrouter import SQLAlchemyCRUDRouter
from src.models.ItensPedido import ItensPedido, ItensPedidoCreate, ItensPedidoModel

from data.database import get_db

itens_pedido_CrudRouter = SQLAlchemyCRUDRouter(
    schema=ItensPedido,
    create_schema=ItensPedidoCreate,
    db_model=ItensPedidoModel,
    db=get_db,
    prefix="itens_pedidos",
)