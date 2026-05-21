from abc import ABC, abstractmethod
# ESTADO ABSTRATO

class EstadoSemaforo(ABC):
    def __init__(self, semaforo):
        self.semaforo = semaforo

    @abstractmethod
    def proximo_estado(self):
        pass

# ESTADOS CONCRETOS
class EstadoVerde(EstadoSemaforo):
    def proximo_estado(self):
        print("Sinal fechando... Indo para o Amarelo.")
        self.semaforo.estado = EstadoAmarelo(self.semaforo)

class EstadoAmarelo(EstadoSemaforo):
    def proximo_estado(self):
        print("Sinal fechou! Indo para o Vermelho.")
        self.semaforo.estado = EstadoVermelho(self.semaforo)
        
class EstadoVermelho(EstadoSemaforo):
    def proximo_estado(self):
        print("Sinal abriu! Indo para o Verde.")
        self.semaforo.estado = EstadoVerde(self.semaforo)

# OBJETO DE CONTEXTO
class Semaforo:
    def __init__(self):
        self.estado = EstadoVermelho(self) # Começa fechado
    def solicitar_mudanca(self):
        self.estado.proximo_estado()

# CLIENTE
sinal = Semaforo()
sinal.solicitar_mudanca() # Saída: Sinal abriu! Indo para o Verde.
sinal.solicitar_mudanca() # Saída: Sinal fechando... Indo para o Amarelo.
sinal.solicitar_mudanca() # Saída: Sinal abriu! Indo para o Verde.
sinal.solicitar_mudanca() # Saída: Sinal fechando... Indo para o Amarelo.