from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from typing import Optional
from data.database import Base

class Categoria(Base):
    __tablename__ = 'categorias'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)

class CategoriaSchema(BaseModel):
    nome: str

    class Config:
        orm_mode = True