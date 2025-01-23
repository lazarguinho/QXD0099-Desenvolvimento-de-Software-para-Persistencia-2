from pydantic import BaseModel
from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from data.database import Base


class ItensPedidoCreate(BaseModel):
    id: int
    preco: float
    quantidade: int
    
class ItensPedido(ItensPedidoCreate):
	id: int
	
	class Config:
		orm_mode = True
  
class ItensPedidoModel(Base):
	__tablename__ = 'itens_pedidos'

	id = Column(Integer, primary_key=True, index=True)
	preco = Column(Float, nullable=False)
	quantidade = Column(Integer, nullable=False)
	pedido_id = Column(Integer, ForeignKey("pedidos.id"), nullable=False)
	produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=False)
	usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
	
	pedido = relationship("PedidoModel", back_populates="itens")
	produto = relationship("ProdutoModel", back_populates="itens")