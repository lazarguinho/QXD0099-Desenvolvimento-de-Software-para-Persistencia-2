from sqlalchemy import Column, Integer, Double
from pydantic import BaseModel
from typing import Optional
from data.database import Base

class ItemPedido(Base):
    __tablename__ = 'itempedidos'

    quantidade = Column(Integer, nullable=False)
    preco = Column(Double, nullable=False)
    
class ItemPedidoSchema(BaseModel):
    quantidade: str
    preco: str

    def subtotal(self):
        return float(self.quantidade) * float(self.preco)
    
    class Config:
        orm_mode = True