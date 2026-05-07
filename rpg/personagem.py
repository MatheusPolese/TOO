from missao import Missao
import random
from missao import MissaoCombate
from missao import MissaoColeta
from missao import MissaoExploracao
from Item import item
from Item import TipoItem

class Personagem:
    def __init__(self, nome):
        self.__nome = nome
        self.__nivel = 1
        self.__vida = 100
        self.__xp = 0
        self.__missoes = []
        self.__ataqueBase = 10
        self.__inventario = []
        self.__arma = None
        self.__vestimenta = None
        self.__utilitario = None

    @property
    def nome(self):
        return self.__nome

    @property
    def inventario(self):
        return self.__inventario

    def add_item(self, item):
        self.__inventario.append(item)
    
    
    
    def calcular_status_totais(self):
        if self.__arma is not None:
            self.__ataqueBase += self.__arma.valorEfeito 
            
        if self.__vestimenta is not None:
            self.__vida += self.__vestimenta.valorEfeito
            
        if self.__utilitario is not None:
            self.__xp += self.__utilitario.valorEfeito

        if self.__vida > 100:
            self.__vida = 100 

        return self.__ataqueBase, self.__vida

    def equipar_item(self, item):
        if item not in self.__inventario:
            print("Item não está no inventário!")
            return
        if item.tipo == TipoItem.ARMA:
            self.__arma = item
        elif item.tipo == TipoItem.VESTIMENTA:
            self.__vestimenta = item
        elif item.tipo == TipoItem.UTILITARIO:
            self.__utilitario = item
        return self.calcular_status_totais()


    @property
    def ataqueBase(self):
        return self.__ataqueBase

    @nome.setter
    def nome(self, valor):
        if valor and isinstance(valor, str):
            self.__nome = valor

    @property
    def nivel(self):
        return self.__nivel

    @property
    def vida(self):
        return self.__vida

    @property
    def xp(self):
        return self.__xp

    def __str__(self):
        return f"Personagem: {self.__nome} (Nível {self.__nivel})"

    def __eq__(self, outro):
        if not isinstance(outro, Personagem):
            return False
        return self.__nome == outro.__nome and self.__nivel == outro.__nivel
    
    def add_missao(self, missao):
        if missao not in self.__missoes:
            self.__missoes.append(missao)
            missao.iniciar_missao() 
        else:
            print(f"O personagem já possui a missão {missao.nome}.")

    def concluir_missao(self, missao, valor):
        if missao in self.__missoes:
            sucesso = missao.concluir_missao(valor) 
            if sucesso:
                self.__xp += missao.recompensa 
                print(f"Sucesso! {self.__nome} ganhou {missao.recompensa} XP.")
                 
            else:
                dano = random.randint(0, 10)
                print(f"Falha na missão {missao.nome}, tomou {dano} de dano.")
                self.__vida = self.__vida - dano
        
        else:
            print("Missão não encontrada com este personagem.")

    def exibir_dados(self):
        print(f"--- Status do Personagem ---")
        print(f"Nome: {self.__nome}")
        print(f"Nível: {self.__nivel}")
        print(f"Vida: {self.__vida}")
        print(f"XP: {self.__xp}")
        print("Inventario:")
        nomes_inventario = [item.nome for item in self.__inventario]
        print(f"Inventário: {nomes_inventario}")
        print(f"Arma: {self.__arma.nome if self.__arma else 'Nenhum'}")
        print(f"Vestimenta: {self.__vestimenta.nome if self.__vestimenta else 'Nenhum'}")
        print(f"Utilitário: {self.__utilitario.nome if self.__utilitario else 'Nenhum'}")

        print("Missões:")
        for m in self.__missoes:
            print(f" - {m}")