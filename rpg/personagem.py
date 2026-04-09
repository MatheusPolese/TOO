class Personagem:
    def __init__(self, nome):
        self.__nome = nome
        self.__nivel = 1
        self.__vida = 100
        self.__xp = 0

    @property
    def nome(self):
        return self.__nome
    
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

    def exibir_dados(self):
        print(f"--- Status do Personagem ---")
        print(f"Nome: {self.__nome}")
        print(f"Nível: {self.__nivel}")
        print(f"Vida: {self.__vida}")
        print(f"XP: {self.__xp}")