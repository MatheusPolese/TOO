from enum import Enum

class Status(Enum):
    PENDENTE = "Pendente"
    EM_ANDAMENTO = "Em Andamento"
    CONCLUIDA = "Concluída"
    FRACASSADA = "Fracassada"