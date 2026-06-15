def salvar_recorde(caminho_arquivo, pontuacao):
    """Salva a pontuação recorde em arquivo texto."""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(str(pontuacao))


def carregar_recorde(caminho_arquivo):
    """Carrega o recorde salvo; retorna 0 se não existir valor válido."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()

            if conteudo == "":
                return 0

            return int(conteudo)

    except FileNotFoundError:
        return 0


def salvar_ranking(caminho_arquivo, ranking):
    """Salva o ranking (lista de tuplas (pontos, tempo)) em arquivo texto."""
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        for pontos, tempo in ranking:
            arquivo.write(f"{pontos};{tempo}\n")


def carregar_ranking(caminho_arquivo):
    """Le o ranking do arquivo. Retorna lista vazia se nao existir."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            ranking = []
            for linha in arquivo:
                linha = linha.strip()
                if linha == "":
                    continue
                pontos, tempo = linha.split(";")
                ranking.append((int(pontos), int(tempo)))
            return ranking
    except FileNotFoundError:
        return []


def atualizar_ranking(ranking, pontos, tempo, limite):
    """Adiciona uma pontuacao e devolve o ranking ordenado, com no maximo `limite` itens.
    Criterio de ordenacao: mais pontos primeiro; em caso de empate, menor tempo primeiro.
    """
    novo = list(ranking) + [(pontos, tempo)]
    novo.sort(key=lambda item: (-item[0], item[1]))
    return novo[:limite]