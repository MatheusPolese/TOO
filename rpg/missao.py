from status import Status

class Missao:
    def __init__(self, nome, descricao, recompensa):
        self.__nome = nome.strip()
        self.__descricao = descricao
        self.__recompensa = recompensa
        self.__status = Status.PENDENTE

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        if valor and valor.strip():
            self.__nome = valor.strip()

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, valor):
        self.__descricao = valor

    @property
    def recompensa(self):
        return self.__recompensa
    
    @recompensa.setter
    def recompensa(self, valor):
        if 1 <= valor <= 50:
            self.__recompensa = valor

    @property
    def status(self):
        return self.__status.value
    
    @status.setter
    def status(self, novo_status):
        fluxo = {
            Status.PENDENTE: Status.EM_ANDAMENTO,
            Status.EM_ANDAMENTO: Status.CONCLUIDA
        }
        if self.__status in fluxo and novo_status == fluxo[self.__status]:
            self.__status = novo_status
        elif novo_status == Status.FRACASSADA:
            self.__status = Status.FRACASSADA

    def __str__(self):
        return f"Missão: {self.__nome} | Status: {self.__status.value}"

    def __eq__(self, outro):
        if not isinstance(outro, Missao):
            return False
        return self.__nome == outro.__nome

    def exibir_dados(self):
        print(f"--- Dados da Missão ---")
        print(f"Nome: {self.__nome}")
        print(f"Descrição: {self.__descricao}")
        print(f"Recompensa: {self.__recompensa} XP")
        print(f"Status: {self.__status.value}")
    
    def iniciar_missao(self):
        return False
    
    def concluir_missao(self) :
        if self.__status == Status.EM_ANDAMENTO:
            self.__status = Status.CONCLUIDA
            print(f"Missão concluída como sucesso. A contabilidade do prêmio de{ self.__recompensa } XP agora está pronta para retirada financeira.")
        else:
            print(f"Erro! missão não pode ser concluida pois está em {self.__status.value}")
    
class MissaoCombate(Missao):
    def __init__(self, nome, descricao, recompensa, tipo_inimigo, inimigos_a_derrotar):
        super().__init__(nome, descricao, recompensa)
        self.__tipo_inimigo = tipo_inimigo
        self.__inimigos_a_derrotar = inimigos_a_derrotar

    def concluir_missao(self, valor):
        if valor >= self._MissaoCombate__inimigos_a_derrotar:
            self._Missao__status = Status.CONCLUIDA
            return True
        self._Missao__status = Status.FRACASSADA
        return False

    @property
    def tipo_inimigo(self):
        return self.__tipo_inimigo
    

    @property
    def inimigos_a_derrotar(self):
        return self.__inimigos_a_derrotar
    
    @tipo_inimigo.setter
    def tipo_inimigo(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__tipo_inimigo = valor.strip()
        else:
            print("Erro: O tipo do inimigo deve ser uma string válida.")

    @inimigos_a_derrotar.setter
    def inimigos_a_derrotar(self, valor):
        if isinstance(valor, int) and valor > 0:
            self.__inimigos_a_derrotar = valor
        else:
            print("Erro: A quantidade de inimigos deve ser um número inteiro positivo.")
    
    def exibir_dados(self):
        print(f"--- Dados da Missão Combate ---")
        print(f"Nome: {self.nome}")
        print(f"Descrição: {self.descricao}")
        print(f"Recompensa: {self.recompensa} XP")
        print(f"Status: {self.status}")
        print(f"Inimigo a derrotar: {self.__inimigos_a_derrotar}")
        print(f"tipo do inimigo: {self.__tipo_inimigo}")     

class MissaoColeta(Missao):

    def __init__(self, nome, descricao, recompensa, item_necessario, quantidade_item):
        super().__init__(nome, descricao, recompensa)
        self.item_necessario = item_necessario
        self.quantidade_item = quantidade_item

    def concluir_missao(self, valor):
        if valor >= self._MissaoColeta__quantidade_item:
            self._Missao__status = Status.CONCLUIDA
            return True
        self._Missao__status = Status.FRACASSADA
        return False

    @property
    def item_necessario(self):
        return self.__item_necessario

    @item_necessario.setter
    def item_necessario(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__item_necessario = valor.strip()
        else:
            print("Erro: O item necessário deve ser uma string.")

    @property
    def quantidade_item(self):
        return self.__quantidade_item

    @quantidade_item.setter
    def quantidade_item(self, valor):
        if isinstance(valor, int) and valor > 0:
            self.__quantidade_item = valor
        else:
            print("Erro: A quantidade deve ser um número inteiro positivo.")

    def exibir_dados(self):
        print(f"--- Dados da Missão Coleta ---")
        print(f"Nome: {self.nome} | Status: {self.status}")
        print(f"Objetivo: Coletar {self.quantidade_item}x {self.item_necessario}")
        print(f"Recompensa: {self.recompensa} XP")

class MissaoExploracao(Missao):
    def __init__(self, nome, descricao, recompensa, regiao_destino, distancia_em_km):
        super().__init__(nome, descricao, recompensa)
        self.regiao_destino = regiao_destino
        self.distancia_em_km = distancia_em_km

    def concluir_missao(self, valor):
        if valor >= self._MissaoExploracao__distancia_em_km:
            self._Missao__status = Status.CONCLUIDA
            return True
        self._Missao__status = Status.FRACASSADA
        return False


    @property
    def regiao_destino(self):
        return self.__regiao_destino

    @regiao_destino.setter
    def regiao_destino(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__regiao_destino = valor.strip()
        else:
            print("Erro: A região de destino deve ser uma string.")

    @property
    def distancia_em_km(self):
        return self.__distancia_em_km

    @distancia_em_km.setter
    def distancia_em_km(self, valor):
        if isinstance(valor, (int, float)) and valor > 0:
            self.__distancia_em_km = float(valor)
        else:
            print("Erro: A distância deve ser um valor numérico positivo.")

    def exibir_dados(self):
        print(f"--- Dados da Missão Exploração ---")
        print(f"Nome: {self.nome} | Status: {self.status}")
        print(f"Destino: {self.regiao_destino} ({self.distancia_em_km} km)")
        print(f"Recompensa: {self.recompensa} XP")