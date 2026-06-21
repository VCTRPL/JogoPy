from src.funcoes import calcular_pontos, jogador_perdeu, limitar_valor, tomar_dano, verificar_colisao
from src.dados import atualizar_ranking
import pygame


def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_jogador_perdeu_com_zero_vidas():
    """Deve indicar derrota quando o total de vidas chega a zero."""
    assert jogador_perdeu(0) is True


def test_jogador_nao_perdeu_com_vidas():
    """Nao deve indicar derrota quando o jogador ainda tem vidas."""
    assert jogador_perdeu(3) is False


def test_limitar_valor_abaixo_do_minimo():
    """Deve retornar o limite minimo quando o valor informado for menor."""
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    """Deve retornar o limite maximo quando o valor informado for maior."""
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    """Deve manter o valor original quando ele ja estiver no intervalo."""
    assert limitar_valor(50, 0, 100) == 50


def test_ranking_insere_e_ordena_por_pontos():
    """Maior pontuacao deve aparecer no topo do ranking."""
    ranking = [(10, 5), (8, 7)]
    novo = atualizar_ranking(ranking, 15, 4, limite=5)
    assert novo[0] == (15, 4)


def test_ranking_respeita_limite():
    """Quando o ranking ja esta cheio, scores menores nao devem entrar."""
    ranking = [(50, 10), (40, 8), (30, 5), (20, 3), (10, 2)]
    novo = atualizar_ranking(ranking, 5, 1, limite=5)
    assert len(novo) == 5
    assert (5, 1) not in novo


def test_ranking_desempata_pelo_menor_tempo():
    """Mesma pontuacao: quem fez em menos tempo vem na frente."""
    ranking = [(20, 30)]
    novo = atualizar_ranking(ranking, 20, 15, limite=5)
    assert novo[0] == (20, 15)


def test_tomar_dano_reduz_vida():
    """Deve subtrair o dano da vida atual corretamente."""
    assert tomar_dano(10, 3) == 7


def test_tomar_dano_zerado():
    """Deve retornar zero quando o dano e igual a vida atual."""
    assert tomar_dano(5, 5) == 0


def test_verificar_colisao_retangulos_sobrepostos():
    """Dois retangulos sobrepostos devem colidir."""
    pygame.init()
    r1 = pygame.Rect(0, 0, 20, 20)
    r2 = pygame.Rect(10, 10, 20, 20)
    assert verificar_colisao(r1, r2) is True
    pygame.quit()


def test_verificar_colisao_retangulos_separados():
    """Dois retangulos sem sobreposicao nao devem colidir."""
    pygame.init()
    r1 = pygame.Rect(0, 0, 20, 20)
    r2 = pygame.Rect(100, 100, 20, 20)
    assert verificar_colisao(r1, r2) is False
    pygame.quit()