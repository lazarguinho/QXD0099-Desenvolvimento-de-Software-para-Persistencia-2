from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from typing import Optional, Set
from data.database import Base
from sqlalchemy import ForeignKey


class ProdutoCreate(BaseModel):
    nome: str
    descricao: str
    preco: str
    imagemUrl: str
    Estoque: int
    categoria_id: int

class Produto(ProdutoCreate):
    id: int

    class Config:
        orm_mode = True
        
class ProdutoModel(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    preco = Column(String, nullable=False)
    imagemUrl = Column(String, nullable=False)
    Estoque = Column(Integer, nullable=False)
    
    categoria_id = Column(Integer, ForeignKey('categorias.id'))  # Chave estrangeira
    categorias = relationship("CategoriaModel", back_populates="produtos")
    itens = relationship("ItensPedidoModel", back_populates="produto")