from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from data.database import Base
from sqlalchemy.orm import relationship

class CategoriaCreate(BaseModel):
    nome: str

class Categoria(CategoriaCreate):
    id: int

    class Config:
        orm_mode = True
        
class CategoriaModel(Base):
    __tablename__ = 'categorias'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    
    produtos = relationship("ProdutoModel", back_populates="categorias")