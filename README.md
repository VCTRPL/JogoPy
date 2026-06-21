# Snakobra

Versao do classico jogo da cobrinha desenvolvida em Python com a biblioteca Pygame.
Projeto final da disciplina de Introducao a Algoritmos / Programacao.

## Integrantes do grupo

- Victor Reis Silva de Paula
- Jose Victor Uliana
- Kaio Vinicius Souza

## Descricao do jogo

O jogador controla uma cobra que se movimenta na tela coletando comida. Cada item coletado
aumenta o tamanho da cobra em um bloco e soma um ponto na pontuacao. O jogo termina quando
a cobra bate na parede, colide com o proprio corpo ou toca a linha que delimita o HUD.

A tela exibe em tempo real a pontuacao atual, o tempo de sobrevivencia em segundos e o
recorde absoluto salvo em arquivo. Ao final da partida e mostrado um ranking com as 5
melhores partidas ja jogadas.

## Objetivo do jogador

Sobreviver o maior tempo possivel e coletar o maximo de comida sem bater nas paredes,
no proprio corpo ou na linha separadora do HUD, alcancando uma pontuacao alta o suficiente
para entrar no Top 5.

## Regras do jogo

- A cobra comeca com 1 bloco e se move continuamente na direcao escolhida.
- Cada comida coletada aumenta o comprimento em 1 e soma 1 ponto.
- Bater na parede encerra a partida.
- Bater no proprio corpo encerra a partida.
- Tocar a linha separadora do HUD encerra a partida.
- Nao e permitido inverter a direcao atual em 180 graus.
- O ranking guarda as 5 melhores partidas; em caso de empate na pontuacao, a partida mais
  curta (menor tempo) fica na frente.

## Controles

- Seta para cima: mover a cobra para cima
- Seta para baixo: mover a cobra para baixo
- Seta para esquerda: mover a cobra para esquerda
- Seta para direita: mover a cobra para direita
- R (na tela de Game Over): jogar de novo
- ESC (na tela de Game Over): sair do jogo

## Estrutura do projeto

```
JogoPy/
├── main.py              # ponto de entrada da aplicacao
├── requirements.txt     # dependencias do projeto
├── src/
│   ├── jogo.py          # loop principal, HUD, campo quadriculado, tela de Game Over
│   ├── config.py        # constantes (tamanho da tela, cores, caminhos de arquivos)
│   ├── dados.py         # leitura e escrita do ranking em arquivo
│   ├── funcoes.py       # funcoes utilitarias de logica pura
│   └── sprites.py       # carregamento e recorte de spritesheet (disponivel para uso futuro)
├── data/
│   └── ranking.txt      # arquivo persistente com o Top 5
├── assets/
│   ├── imagens/         # spritesheet e elementos visuais
│   ├── sons/            # trilha sonora (musica.ogg, opcional)
│   └── fontes/          # fontes externas (opcional)
├── tests/
│   └── test_logica.py   # testes automatizados com pytest
└── docs/
    └── proposta.MD      # proposta inicial do projeto
```

## Visual do jogo

- O campo de jogo e exibido com um tabuleiro quadriculado alternando dois tons de verde.
- Uma linha horizontal separa o HUD (pontos, tempo, recorde) da area de jogo.
- A cobra e desenhada em verde com uma borda escura para contraste com o campo.

## Como executar o projeto

```bash
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Musica de fundo (opcional)

O jogo procura por um arquivo de musica em `assets/sons/musica.ogg` e toca em loop se
estiver presente. Caso o arquivo nao exista, o jogo roda normalmente em silencio.

Para adicionar uma trilha, baixe um arquivo livre (sugestao: Kenney Assets, OpenGameArt
ou itch.io) e salve como `assets/sons/musica.ogg`.

## Creditos de assets

Nenhum asset externo esta sendo usado nesta versao. Graficos sao desenhados via
`pygame.draw`, sem imagens externas; fonte de sistema padrao do Pygame.
