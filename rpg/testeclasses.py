
from status import Status
from missao import Missao
from missao import MissaoCombate
from missao import MissaoColeta
from missao import MissaoExploracao

print("Teste missão padrao")
missao_padrao = Missao("Missao padrao", "faça isso", 10)
missao_padrao.iniciar_missao()
missao_padrao.concluir_missao()
missao_padrao.exibir_dados()

print("\nTeste missão combate")
missao_combate = MissaoCombate("O resgate", "resgatar tesouros", 20,"bandido",5)
missao_combate.iniciar_missao()
missao_combate.concluir_missao()
missao_combate.exibir_dados()

print("\nTeste missão coleta")
missao_coleta = MissaoColeta("coleta", "coletar frutas", 30,"cesta",1)
missao_coleta.iniciar_missao()
missao_coleta.concluir_missao()
missao_coleta.exibir_dados()

print("\nTeste missão explorar")
missao_explorar = MissaoExploracao("O resgate", "resgatar tesouros", 20,"Vales do Sul",10)
missao_explorar.iniciar_missao()
missao_explorar.concluir_missao()
missao_explorar.exibir_dados()

