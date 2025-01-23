from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from typing import Optional, List
from data.database import Base
from sqlalchemy.orm import relationship


class UsuarioCreate(BaseModel):
    nome: str
    email: str
    telefone: str
    senha: str
    
class Usuario(UsuarioCreate):
    id: int
    
    class Config:
        orm_mode = True
        
class UsuarioModel(Base):
    __tablename__ = 'usuarios'
           
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    telefone = Column(String, unique=True, nullable=True)
    senha = Column(String, nullable=False)
    
    pedidos = relationship("PedidoModel", back_populates="usuario")