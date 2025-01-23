from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from data.database import Base


class PedidoCreate(BaseModel):
    data: str
    status: str
    produto_id: int

class Pedido(PedidoCreate):
    id: int
    
    class Config:
        orm_mode = True 

class PedidoModel(Base):
    __tablename__ = 'pedidos'

    id = Column(Integer, primary_key=True, index=True)
    data = Column(String, nullable=False)
    status = Column(String, nullable=False)
    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    
    pagamento = relationship("PagamentoModel", back_populates="pedido")    
    usuario = relationship("UsuarioModel", back_populates="pedidos")
    itens = relationship("ItensPedidoModel", back_populates="pedido")