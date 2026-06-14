import pygame
import time
import random
from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    CINZA,
    BRANCO,
    PRETO,
    CAMINHO_RECORDE,
    CAMINHO_SPRITES,
)

from src.funcoes import (
    calcular_pontos,
    jogador_perdeu,
    limitar_valor,
    verificar_colisao,
    tomar_dano,
)

from src.sprites import pegar_sprite
from src.dados import (
    salvar_recorde,
    carregar_recorde,
)

def executar_jogo():
    pygame.init()

    #Configuração da tela
    largura = LARGURA_TELA
    altura = ALTURA_TELA
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption(TITULO_JOGO + " - Snakobra")

    #Cores do jogo
    BRANCO = (255, 255, 255)
    VERDE = (0, 255, 0)
    PRETO = (0, 0, 0)
    VERMELHO = (255, 0, 0)

    #Criação do relógio
    clock = pygame.time.Clock()
    velocidade = 10 #Quanto maior o número, maior a velocidade da cobrinha

    #Tamanho do bloco(Cobra e comida)
    tamanho_bloco = 20 #Quanto maior o número, maior o tamanho da cobrinha e da comida

    #Fonte
    fonte = pygame.font.SysFont(None, 35)

    #Função para mostrar a pontuação na tela
    def mostrar_pontuacao(pontos):
        valor = fonte.render("Pontuação: " + str(pontos), True, PRETO)
        tela.blit(valor, [10, 10]) #Exibe o valor no ponto superior esquerdo da tela

    #Função principal
    def jogo():
        #Definir a posição inicial da cobrinha
        x = largura // 2
        y = altura // 2
        x_mudanca = 0
        y_mudanca = 0

        cobra = []
        comprimento_cobra = 1

        #Gerar aleatória para a comida
        comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20) * 20
        comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20) * 20

        fim_de_jogo = False #Controla se o jogo termina ou não

        while not fim_de_jogo:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    fim_de_jogo = True
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT and x_mudanca != tamanho_bloco:
                        x_mudanca = -tamanho_bloco
                        y_mudanca = 0
                    elif evento.key == pygame.K_RIGHT and x_mudanca != -tamanho_bloco:
                        x_mudanca = tamanho_bloco
                        y_mudanca = 0
                    elif evento.key == pygame.K_UP and y_mudanca != tamanho_bloco:
                        y_mudanca = -tamanho_bloco
                        x_mudanca = 0
                    elif evento.key == pygame.K_DOWN and y_mudanca != -tamanho_bloco:
                        y_mudanca = tamanho_bloco
                        x_mudanca = 0

            #Atualizar a posição da cobrinha
            x += x_mudanca
            y += y_mudanca

            #Verificar se a cobra bateu na borda
            if x >= largura or x < 0 or y >= altura or y < 0:
                fim_de_jogo = True

            tela.fill(BRANCO) #Limpa a tela com a cor branca

            pygame.draw.rect(tela, VERMELHO, [comida_x, comida_y, tamanho_bloco, tamanho_bloco]) #Define a cor, e no X/Y o tamanho do bloco

            cabeca = [] #Lista para armazenar a posição da cabeça da cobra
            cabeca.append(x)
            cabeca.append(y)
            cobra.append(cabeca) #Adiciona a posição da cabeça da cobra à lista da cobra da linha 68

            if len(cobra) > comprimento_cobra:
                del cobra[0] #Remove a cauda da cobra para que ela se mova

            #Verifica se a cobra bateu nela mesma
            for bloco in cobra[:-1]: #Verifica se a cabeça da cobra bateu com algum bloco do corpo, exceto a cabeça (último bloco)
                if bloco == cabeca:
                    fim_de_jogo = True

            #Desenha todos os blocos da cobra
            for bloco in cobra:
                pygame.draw.rect(tela, VERDE, [bloco[0], bloco[1], tamanho_bloco, tamanho_bloco])

            #Mostrar a pontuação
            mostrar_pontuacao(comprimento_cobra - 1) #A pontuação é o comprimento da cobra menos 1, pq a cobra começa com comprimento == 1

            pygame.display.update() #Atualiza a tela

            #Verifica se a cobra comeu a comida
            if x == comida_x and y == comida_y:
                comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20) * 20
                comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20) * 20
                comprimento_cobra += 1 #Aumenta o comprimento da cobra quando ela come a comida

            clock.tick(velocidade) #Controla a velocidade do jogo

        #Quando o jogo terminar
        tela.fill(BRANCO)
        mensagem = fonte.render("Game Over! PONTUAÇÃO: " + str(comprimento_cobra - 1), True, VERMELHO)
        tela.blit(mensagem, [largura // 2 - 150, altura // 2 - 50]) #Exibe a mensagem de Game Over no centro da tela
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()

    jogo()