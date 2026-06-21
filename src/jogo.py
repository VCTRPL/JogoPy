import pygame
import random

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    TITULO_JOGO,
    BRANCO,
    PRETO,
    CAMINHO_RANKING,
    CAMINHO_MUSICA,
    TAMANHO_RANKING,
)
from src.dados import (
    carregar_ranking,
    salvar_ranking,
    atualizar_ranking,
)

# Constantes especificas do Snake
VELOCIDADE = 10        # quadros por segundo (velocidade da cobra)
TAMANHO_BLOCO = 20     # tamanho em pixels de cada bloco
ALTURA_HUD = 40        # faixa do topo reservada para pontos/tempo/recorde
VERDE = (0, 200, 0)
VERMELHO = (255, 0, 0)


def tocar_musica():
    """Toca musica de fundo em loop se o arquivo existir; ignora se faltar."""
    try:
        pygame.mixer.music.load(CAMINHO_MUSICA)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)  # -1 = repete pra sempre
    except (pygame.error, FileNotFoundError):
        pass


def sortear_comida():
    """Sorteia uma posicao alinhada ao grid, sempre abaixo da HUD."""
    x = random.randrange(0, LARGURA_TELA - TAMANHO_BLOCO, TAMANHO_BLOCO)
    y = random.randrange(ALTURA_HUD, ALTURA_TELA - TAMANHO_BLOCO, TAMANHO_BLOCO)
    return x, y


def desenhar_hud(tela, fonte, pontos, tempo, recorde):
    """Mostra pontos, tempo e recorde no topo da tela."""
    texto = f"Pontos: {pontos}   Tempo: {tempo}s   Recorde: {recorde}"
    tela.blit(fonte.render(texto, True, PRETO), (10, 10))


def tela_game_over(tela, fonte, pontos, tempo, ranking):
    """Mostra placar e top 5. Retorna True se o jogador quer reiniciar."""
    tela.fill(BRANCO)
    tela.blit(fonte.render("GAME OVER", True, VERMELHO),
              (LARGURA_TELA // 2 - 70, 30))
    tela.blit(fonte.render(f"Sua pontuacao: {pontos}    Tempo: {tempo}s", True, PRETO),
              (LARGURA_TELA // 2 - 150, 70))
    tela.blit(fonte.render("RANKING (TOP 5)", True, PRETO),
              (LARGURA_TELA // 2 - 90, 120))

    for i, (p, t) in enumerate(ranking):
        linha = f"{i + 1}.   {p} pts   -   {t}s"
        tela.blit(fonte.render(linha, True, PRETO),
                  (LARGURA_TELA // 2 - 90, 155 + i * 28))

    tela.blit(fonte.render("R = jogar de novo     ESC = sair", True, PRETO),
              (LARGURA_TELA // 2 - 160, ALTURA_TELA - 30))
    pygame.display.update()

    # Espera o jogador decidir
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    return True
                if evento.key == pygame.K_ESCAPE:
                    return False


def partida(tela, fonte, relogio, recorde):
    """Executa uma partida do Snake.
    Retorna (pontos, tempo_em_segundos, fechou_janela)."""
    # Posicao e direcao iniciais
    x = LARGURA_TELA // 2
    y = ALTURA_TELA // 2
    dx, dy = 0, 0

    cobra = []
    comprimento = 1
    comida_x, comida_y = sortear_comida()

    inicio = pygame.time.get_ticks()
    fim = False
    fechou = False

    while not fim:
        # 1. Eventos: teclado e clique no X da janela
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim = True
                fechou = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -TAMANHO_BLOCO, 0
                elif evento.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = TAMANHO_BLOCO, 0
                elif evento.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -TAMANHO_BLOCO
                elif evento.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, TAMANHO_BLOCO

        if fechou:
            break

        # 2. Move a cabeca
        x += dx
        y += dy

        # 3. Bateu na parede (ou na faixa da HUD)? Acaba o jogo
        if x < 0 or x >= LARGURA_TELA or y < ALTURA_HUD or y >= ALTURA_TELA:
            fim = True
            continue

        # 4. Atualiza a lista que representa o corpo
        cabeca = [x, y]
        cobra.append(cabeca)
        if len(cobra) > comprimento:
            del cobra[0]

        # 5. Bateu em si mesma?
        for bloco in cobra[:-1]:
            if bloco == cabeca:
                fim = True

        # 6. Comeu a comida?
        if x == comida_x and y == comida_y:
            comida_x, comida_y = sortear_comida()
            comprimento += 1

        # 7. Desenha tudo
        tela.fill(BRANCO)
        pygame.draw.rect(tela, VERMELHO, [comida_x, comida_y, TAMANHO_BLOCO, TAMANHO_BLOCO])
        for bloco in cobra:
            pygame.draw.rect(tela, VERDE, [bloco[0], bloco[1], TAMANHO_BLOCO, TAMANHO_BLOCO])

        pontos = comprimento - 1
        tempo = (pygame.time.get_ticks() - inicio) // 1000
        desenhar_hud(tela, fonte, pontos, tempo, recorde)
        # Linha separando a HUD da area de jogo
        pygame.draw.line(tela, PRETO, (0, ALTURA_HUD), (LARGURA_TELA, ALTURA_HUD), 1)

        pygame.display.update()
        relogio.tick(VELOCIDADE)

    tempo_final = (pygame.time.get_ticks() - inicio) // 1000
    return comprimento - 1, tempo_final, fechou


def executar_jogo():
    """Ponto de entrada chamado pelo main.py."""
    pygame.init()
    pygame.mixer.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO + " - Snakobra")

    fonte = pygame.font.SysFont(None, 28)
    relogio = pygame.time.Clock()

    tocar_musica()

    continuar = True
    while continuar:
        ranking = carregar_ranking(CAMINHO_RANKING)
        recorde = ranking[0][0] if ranking else 0

        pontos, tempo, fechou = partida(tela, fonte, relogio, recorde)

        if fechou:
            break

        ranking = atualizar_ranking(ranking, pontos, tempo, TAMANHO_RANKING)
        salvar_ranking(CAMINHO_RANKING, ranking)

        continuar = tela_game_over(tela, fonte, pontos, tempo, ranking)

    pygame.quit()
