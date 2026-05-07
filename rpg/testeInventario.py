
from status import Status
from missao import Missao
from missao import MissaoCombate
from missao import MissaoColeta
from missao import MissaoExploracao
from Item import item
from Item import TipoItem
from personagem import Personagem


p1 = Personagem("matheus")

p1.exibir_dados()

m1 = MissaoColeta("coleta 1", "coletar 5 ervas", 20, "erva", 5)
m2 = MissaoExploracao("passo fundo", "viajar 10km", 30, "Sul", 10)
espada = item("Espada de Ferro", "Aumenta o ataque", TipoItem.ARMA, 10)
armadura = item("Peitoral de Aço", "Aumenta a vida em 10%", TipoItem.VESTIMENTA, 10)
amuleto = item("Amuleto Místico", "Aumenta a vida em 5%", TipoItem.UTILITARIO, 5)

p1.add_item(espada)
p1.add_item(armadura)
p1.add_item(amuleto)

x=str(input("deseja equipar sua arma? [SIM] - [NÃO]: "))
if x == "SIM":
    p1.equipar_item(espada)
x=str(input("deseja equipar sua VESTIMENTA? [SIM] - [NÃO]: "))
if x == "SIM":   
    p1.equipar_item(armadura)

p1.add_missao(m1)
p1.add_missao(m2)

print("\n--- Simulando Jornada ---")
p1.concluir_missao(m1, 100) 
p1.concluir_missao(m2, 5)  


p1.exibir_dados() 