from enum import Enum

class StatusEntrega(str, Enum):
    PENDENTE = "pendente"
    EM_TRANSITO = "em_transito"
    ENTREGUE = "entregue"
    CANCELADO = "cancelado"