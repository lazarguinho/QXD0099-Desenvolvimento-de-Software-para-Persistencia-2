from fastapi import FastAPI
from .routes.UsuarioRoutes import usuario_router, usuario_CrudRouter
from .routes.CategoriaRoutes import categoria_CrudRouter
from .routes.PagamentoRoutes import pagamento_CrudRouter
from .routes.PedidoRoutes import pedido_CrudRouter
from .routes.ProdutoRoutes import produto_CrudRouter
from .routes.ItensPedido import itens_pedido_CrudRouter
from .routes.GetNumeroEntidadesRoutes import quantidades_router

from data.database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(usuario_router)
app.include_router(usuario_CrudRouter)
app.include_router(categoria_CrudRouter)
app.include_router(pagamento_CrudRouter)
app.include_router(pedido_CrudRouter)
app.include_router(itens_pedido_CrudRouter)
app.include_router(produto_CrudRouter)
app.include_router(quantidades_router)

@app.get('/')
def read_root():
    return { "message": "Bem vindo"}