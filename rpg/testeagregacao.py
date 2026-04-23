from personagem import Personagem
from missao import MissaoColeta, MissaoExploracao

p1 = Personagem("matheus")

m1 = MissaoColeta("coleta 1", "coletar 5 ervas", 20, "erva", 5)
m2 = MissaoExploracao("passo fundo", "viajar 10km", 30, "Sul", 10)

p1.add_missao(m1)
p1.add_missao(m2)

print("\n--- Simulando Jornada ---")
p1.concluir_missao(m1, 5) 
p1.concluir_missao(m2, 2)  


p1.exibir_dados() 