from fastapi import FastAPI
from .routes.UsuarioRoutes import usuario_router
from .routes.CategoriaRoutes import categoria_router
from .routes.PagamentoRoutes import pagamento_router
from .routes.PedidoRoutes import pedido_router
from .routes.ProdutoRoutes import produto_router
from .routes.ItensPedido import itens_pedido_router

from data.database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(usuario_router)
app.include_router(categoria_router)
app.include_router(pagamento_router)
app.include_router(pedido_router)
app.include_router(itens_pedido_router)
app.include_router(produto_router)

@app.get('/')
def read_root():
    return { "message": "Bem vindo"}