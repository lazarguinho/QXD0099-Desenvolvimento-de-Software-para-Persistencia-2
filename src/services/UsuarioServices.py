from src.models.Usuario import Usuario, UsuarioModel
from sqlalchemy import func
from sqlalchemy.orm import Session

def verificar_usuario_existe(usuario_id: int) -> bool:
    return True

def adicionar_usuario(usuario: Usuario):
    pass

def count_usuarios(db: Session):
    return db.query(func.count(UsuarioModel.id)).scalar()