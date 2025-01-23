from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from data.database import get_db
from src.models.Usuario import UsuarioModel
from src.models.Categoria import CategoriaModel
from src.models.Produto import ProdutoModel
from src.models.Pedido import PedidoModel
from src.models.Pagamento import PagamentoModel
from src.models.ItensPedido import ItensPedidoModel
from src.utils.logging_config import logger

quantidades_router = APIRouter(prefix="/quantidade", tags=["Quantidade de Entidades"])

@quantidades_router.get("/usuarios", summary="Retorna a quantidade total de usuários cadastrados")
def get_quantidade_usuarios(db: Session = Depends(get_db)):
    quantidade = db.query(UsuarioModel).count()
    logger.info(f"Numero entidades 'Usuario' cfornecido com sucesso")
    return {"quantidade": quantidade}

@quantidades_router.get("/categorias", summary="Retorna a quantidade total de categorias cadastradas")
def get_quantidade_categorias(db: Session = Depends(get_db)):
    quantidade = db.query(CategoriaModel).count()
    logger.info(f"Numero entidades 'Categoria' cfornecido com sucesso")
    return {"quantidade": quantidade}

@quantidades_router.get("/produtos", summary="Retorna a quantidade total de produtos cadastrados")
def get_quantidade_produtos(db: Session = Depends(get_db)):
    quantidade = db.query(ProdutoModel).count()
    logger.info(f"Numero entidades 'Produto' cfornecido com sucesso")
    return {"quantidade": quantidade}

@quantidades_router.get("/pedidos", summary="Retorna a quantidade total de pedidos cadastrados")
def get_quantidade_pedidos(db: Session = Depends(get_db)):
    quantidade = db.query(PedidoModel).count()
    logger.info(f"Numero entidades 'Pedido' cfornecido com sucesso")
    return {"quantidade": quantidade}

@quantidades_router.get("/pagamentos", summary="Retorna a quantidade total de pagamentos cadastrados")
def get_quantidade_pagamentos(db: Session = Depends(get_db)):
    quantidade = db.query(PagamentoModel).count()
    logger.info(f"Numero entidades 'Pagamento' cfornecido com sucesso")
    return {"quantidade": quantidade}

@quantidades_router.get("/itens_pedidos", summary="Retorna a quantidade total de itens de pedidos cadastrados")
def get_quantidade_itens_pedidos(db: Session = Depends(get_db)):
    quantidade = db.query(ItensPedidoModel).count()
    logger.info(f"Numero entidades 'ItensPedido' cfornecido com sucesso")
    return {"quantidade": quantidade}

@quantidades_router.get("/total", summary="Retorna a soma total de todas as entidades cadastradas")
def get_total_entidades(db: Session = Depends(get_db)):
    total_usuarios = db.query(UsuarioModel).count()
    total_categorias = db.query(CategoriaModel).count()
    total_produtos = db.query(ProdutoModel).count()
    total_pedidos = db.query(PedidoModel).count()
    total_pagamentos = db.query(PagamentoModel).count()
    total_itens_pedidos = db.query(ItensPedidoModel).count()

    total = (
        total_usuarios +
        total_categorias +
        total_produtos +
        total_pedidos +
        total_pagamentos +
        total_itens_pedidos
    )
    logger.info(f"Numero total de entidades fornecido com sucesso")
    return {
        "total": total,
        "detalhes": {
            "usuarios": total_usuarios,
            "categorias": total_categorias,
            "produtos": total_produtos,
            "pedidos": total_pedidos,
            "pagamentos": total_pagamentos,
            "itens_pedidos": total_itens_pedidos
        }
    }
