from src.models.Categoria import Categoria

def verificar_categoria(categoria_id):
    categoria = Categoria.query.filter_by(id=categoria_id).first()
    if not categoria:
        raise Exception("Categoria não encontrada")
    return categoria

def adicionar_categoria(nome):
    categoria = Categoria(nome=nome)
    categoria.save()
    return categoria