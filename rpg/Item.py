from enum import Enum

class TipoItem(Enum):
    ARMA = "ARMA"
    VESTIMENTA = "VESTIMENTA"
    UTILITARIO = "UTILITARIO"
   ## ARMA = "faca", "revolver", "garrafa de vidro"
    #VESTIMENTA = "armadura de correntes", "trapos"
    #UTILITARIO = "pocao", "livro"


class item:
    def __init__(self, nome, descricao, tipo, valorEfeito):
        self.__nome = nome.strip()
        self.__descricao = descricao
        self.__tipo = tipo
        self.__valorEfeito = float(valorEfeito)

    @property
    def nome(self):
        return self.__nome

    @property
    def descricao(self):  
        return self.__descricao
    
    @property
    def valorEfeito(self):
        return self.__valorEfeito
    
    @property
    def tipo(self):
        return self.__tipo