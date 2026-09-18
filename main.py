#Trabalho de Miguel Machado Pinheiro 2026.2

from PPlay.window import Window 
from PPlay.sprite import Sprite
from PPlay.gameimage import GameImage
from PPlay.sprite import Sprite

janela = Window(800, 601, "Natureza Sinfonica") #Cria a Janela com o nome e tamanho especificado
fundo = GameImage("Assets/Arenas/arenaF.png") #Cria a imagem de fundo
bossF = Sprite("Assets/Boss/bossF.png") #Cria a imagem do boss
prota = Sprite("Assets/Protagonista/protagonista.png") #Cria a imagem do protagonista

#Variáveis de largura e altura da janela para a barra de vida e mana
L = janela.width
A = janela.height

#Barras de vida e mana do jogador e do boss, setando as suas posições na tela
barra_vida_jogador = Sprite("Assets/HUD/barra_vida_jogador.png")
barra_vida_jogador.set_position(L * 0.04, A * 0.07) 

barra_mana_jogador = Sprite("Assets/HUD/barra_mana_jogador.png")
barra_mana_jogador.set_position(L * 0.04, A * 0.15)

barra_vida_boss = Sprite("Assets/HUD/barra_vida_boss.png")
barra_vida_boss.set_position(L * 0.96 - barra_vida_boss.width, A * 0.07)

linha_do_chao = 430 #Define a linha do chão

bossF.x = janela.width - bossF.width - 10 #Coloca o boss no canto direito da tela
bossF.y = linha_do_chao - bossF.height #Coloca o boss na linha do chão

prota.x = 10 #Coloca o protagonista no canto esquerdo da tela
prota.y = linha_do_chao - prota.height #Coloca o protagonista na linha do chão

#Loop que faz a tela rodar
while True:
    #Coloca a imagem de fundoo (TEM QUE VIR PRIMEIRO)
    fundo.draw()
    bossF.draw()
    prota.draw()
    barra_vida_jogador.draw()
    barra_mana_jogador.draw()
    barra_vida_boss.draw()

    janela.update()