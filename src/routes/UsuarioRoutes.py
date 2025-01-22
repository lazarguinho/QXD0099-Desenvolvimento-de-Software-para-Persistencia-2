from fastapi_crudrouter import SQLAlchemyCRUDRouter
from src.models.Usuario import Usuario, UsuarioSchema
from src.services.UsuarioServices import verificar_usuario_existe, adicionar_usuario
from data.database import get_db


usuario_router = SQLAlchemyCRUDRouter(
    schema=UsuarioSchema,  # Modelo
    db_model=Usuario,  # Tabela no BD
    db=get_db,  # Sessão do BD
    prefix="usuarios",  # Prefixo das rotas
    tags=["Usuários"]
)





# from fastapi import APIRouter, HTTPException
# from fastapi.responses import FileResponse
# from typing import Optional, List
# from src.models.Carta import Carta
# from src.services.CartaService import verificar_carta_existe, adicionar_carta, filtrar_cartas, calcular_hash_csv, ler_dados_csv, escrever_dados_csv, CSV_FILE_PATH
# from src.utils.logging_config import logger
# import zipfile
# import os

# router = APIRouter()

# @router.post("/")
# def criar_carta(carta: Carta):
#     if verificar_carta_existe(carta.id):
#         logger.error(f"Ao tentar adicionar um carta com id {carta.id} ja existente.")
#         raise HTTPException(status_code=400, detail="Uma carta com este ID já existe.")
    
#     adicionar_carta(carta)
#     logger.info(
#         f"Carta inserida com sucesso: id={carta.id}, nome={carta.nome}, tipo={carta.tipo}, "
#         f"custo={carta.custo}, cor={carta.cor}, rarity={carta.rarity}, habilidade={carta.habilidade}"
#     )
#     return {"message": "Carta adicionada com sucesso!"}

# @router.get("/filtrar/", response_model=List[Carta])
# def listar_cartas_filtradas(tipo: Optional[str] = None, cor: Optional[str] = None, rarity: Optional[str] = None):
#     logger.info(f"Listando cartas filtradas: tipo={tipo}, cor={cor}, rarity={rarity}")
#     return filtrar_cartas(tipo, cor, rarity)

# @router.get("/hash/")
# def calcular_hash():
#     try:
#         logger.info("Hash SHA256 do arquivo CSV calculado.")
#         return {"hash": calcular_hash_csv()}
#     except Exception as e:
#         logger.error(f"Erro ao calcular o hash SHA256: {str(e)}")
#         raise HTTPException(status_code=500, detail=str(e))

# @router.get("/", response_model=List[Carta])
# def listar_todas_cartas():
#     logger.info("Todas as cartas listadas")
#     return ler_dados_csv()

# @router.get("/{id}")
# def listar_carta_por_id(id: int):
# 	cartas = ler_dados_csv()
# 	for carta in cartas:
# 		if carta.id == id:
# 			logger.info(f"Carta: {id} listada com sucesso")
# 			return carta
# 	logger.error(f"Ao listar carta: {id}")
# 	raise HTTPException(status_code=404, detail='Carta não encontrada')

# @router.put("/{carta_id}", response_model=Carta)
# def atualizar_carta(carta_id: int, carta_atualizada: Carta):
#     cartas = ler_dados_csv()
#     for i, carta in enumerate(cartas):
#         if carta.id == carta_id:
#             cartas[i] = carta_atualizada
#             escrever_dados_csv(cartas)
#             logger.info(f"Carta {carta_id} atualizada com sucesso")
#             return carta_atualizada
#     logger.error(f"Ao editar carta")
#     raise HTTPException(status_code=404, detail="Carta não encontrada")

# @router.delete("/{carta_id}", response_model=dict)
# def deletar_carta(carta_id: int):
#     cartas = ler_dados_csv()
#     cartas_filtradas = [carta for carta in cartas if carta.id != carta_id]
#     if len(cartas) == len(cartas_filtradas):
#         logger.error(f"Ao deletar carta: {carta_id}")
#         raise HTTPException(status_code=404, detail="Carta não encontrada")
#     escrever_dados_csv(cartas_filtradas)