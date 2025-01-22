from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from typing import Optional
from data.database import Base

class Usuario(Base):
    __tablename__ = 'usuarios'
           
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    telefone = Column(String, unique=True, nullable=True)
    senha = Column(String, nullable=False)
    
    
class UsuarioSchema(BaseModel):
    nome: str
    email: str
    telefone: Optional[str]
    senha: str
    
    class Config:
        orm_mode = True