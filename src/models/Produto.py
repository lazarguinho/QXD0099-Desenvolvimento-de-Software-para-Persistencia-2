from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from typing import Optional
from data.database import Base

class Produto(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    preco = Column(String, nullable=False)
    imagemUrl = Column(String, nullable=False)

    pedidos = relationship("ItemPedido", back_populates="produto")

class ProdutoSchema(BaseModel):
    nome: str
    descricao: str
    preco: str
    imagemUrl: str

    class Config:
        orm_mode = True