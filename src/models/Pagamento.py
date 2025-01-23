from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from data.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class PagamentoCreate(BaseModel):
    data: str
    
class Pagamento(PagamentoCreate):
    id: int
    
    class Config:
        orm_mode = True

class PagamentoModel(Base):
    __tablename__ = 'pagamentos'

    id = Column(Integer, primary_key=True, index=True)
    data = Column(String, nullable=False)
    
    pedido_id = Column(Integer, ForeignKey("pedidos.id"), nullable=False)
    pedido = relationship("PedidoModel", back_populates="pagamento")