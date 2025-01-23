from sqlalchemy import Column, Integer, DateTime
from pydantic import BaseModel
from typing import Optional
from data.database import Base
from datetime import datetime

class Pagamento(Base):
    __tablename__ = 'pagamentos'

    id = Column(Integer, primary_key=True, index=True)
    data = Column(DateTime, nullable=False, default=datetime.utcnow)

class PagamentoSchema(BaseModel):
    data: datetime

    class Config:
        orm_mode = True