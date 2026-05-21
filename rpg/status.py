from abc import ABC, abstractmethod

# ESTADO ABSTRATO

class EstadoMissao(ABC):
    def __init__(self, missao):
        self._missao = missao

    @property
    def missao(self):
        return self._missao
    
    @property
    @abstractmethod
    def nome(self):
        pass

    @abstractmethod
    def iniciar(self):
        pass

    @abstractmethod
    def concluir(self, valor):
        pass

class EstadoPendente(EstadoMissao):
    @property
    def nome(self):
        return "Pendente"

    def iniciar(self):
        # Transiciona para Em Andamento
        self.missao.estado = EstadoAndamento(self.missao)
        print(f"A missão '{self.missao.nome}' foi iniciada com sucesso!")
        return True

    def concluir(self, valor):
        print(f"Erro: Não é possível concluir uma missão que ainda está Pendente.")
        return False
    
class EstadoAndamento(EstadoMissao):
    @property
    def nome(self):
        return "Em Andamento"
    
    def iniciar(self):
        print (f"Missão '{self.missao.nome}' já está em andamento ")
        return False
    
    def concluir(self, valor):
        if self.missao.verificar_sucesso(valor):
            self.missao.estado = EstadoConcluida(self.missao)
            print(f"Missão concluída com sucesso! Recompensa de {self.missao.recompensa} XP pronta para retirada.")
            return True
        else:
            self.missao.estado = EstadoFracassada(self.missao)
            print(f"Que pena! Você fracassou na missão '{self.missao.nome}'.")
            return False
       
class EstadoConcluida(EstadoMissao):
    @property
    def nome(self):
        return "Concluída"

    def iniciar(self):
        print("Erro: Esta missão já foi concluída com sucesso. Não pode ser reiniciada.")
        return False

    def concluir(self, valor):
        print("Aviso: Esta missão já se encontra concluída.")
        return False
    
class EstadoFracassada(EstadoMissao):
    @property
    def nome(self):
        return "Fracassada"

    def iniciar(self):
        print("Erro: Esta missão foi fracassada. Você não pode reiniciá-la.")
        return False

    def concluir(self, valor):
        print("Aviso: Esta missão já foi finalizada como Fracassada.")
        return False