from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from typing import Optional
from data.database import Base
from datetime import datetime

class Pedido(Base):
    __tablename__ = 'pedidos'

    id = Column(Integer, primary_key=True, index=True)
    data = Column(DateTime, nullable=False, default=datetime.utcnow)
    status = Column(String, nullable=False)
    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=False)

    produtos = relationship("ItemPedido", back_populates="pedido")

class PedidoSchema(BaseModel):
    data: datetime
    status: str

    def total(self):
        return sum(item.preco for item in self.items)
    
    class Config:
        orm_mode = True