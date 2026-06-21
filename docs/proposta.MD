# Proposta Inicial do Jogo

## 1. Nome provisório do jogo

**Snakobra**

## 2. Integrantes do grupo

- Nome 1: Victor Reis Silva de Paula
- Nome 2: José Victor Uliana
- Nome 3: Kaio Vinicius Souza

## 3. Tipo de jogo

Snake

## 4. Descrição geral do jogo

Na tela aparece uma cobra e um item de comida em posição aleatória. O jogador controla a direção da cobra usando as setas do teclado. O objetivo é coletar os itens de comida, fazendo a cobra crescer e a pontuação aumentar. O desafio é evitar colidir com as bordas da tela, com o próprio corpo da cobra ou com a linha que delimita o HUD.

## 5. Objetivo do jogador

Coletar o maior número possível de itens de comida, fazendo a cobra crescer e acumulando a maior pontuação possível, buscando uma vaga no Top 5 do ranking.

## 6. Regras principais

- A cobra se move continuamente na direção atual, sem parar.
- O jogador muda a direção usando as setas do teclado.
- Não é possível inverter a direção diretamente (ex.: ir para cima enquanto está se movendo para baixo).
- Cada item de comida coletado vale 1 ponto e faz a cobra crescer em 1 bloco.
- A comida reaparece em posição aleatória após ser coletada.
- Uma linha horizontal separa o HUD da área de jogo; a cobra não pode cruzá-la.

## 7. Condição de vitória

Não há condição de vitória absoluta. O objetivo é sobreviver o máximo possível e alcançar a maior pontuação para entrar no Top 5 do ranking.

## 8. Condição de derrota ou encerramento

A partida termina quando a cobra colide com a borda da tela, com o próprio corpo ou com a linha separadora do HUD. O jogador também pode encerrar manualmente pressionando ESC na tela de Game Over ou fechando a janela.

## 9. Elementos previstos no jogo

### Jogador ou elemento principal

A cobra, representada por uma lista de posições que formam seu corpo. É controlada pelas setas do teclado e cresce ao coletar comida.

### Obstáculos, inimigos ou desafios

O próprio corpo da cobra, as bordas da tela e a linha separadora do HUD funcionam como obstáculos. À medida que a cobra cresce, desviar do próprio corpo se torna progressivamente mais difícil.

### Itens, alvos ou objetos de interação

Itens de comida que aparecem em posição aleatória na área de jogo (abaixo do HUD). Ao ser coletado, o item some e reaparece em outro lugar.

### Pontuação, vidas, tempo e progresso

A pontuação, o tempo de sobrevivência e o recorde são exibidos no HUD. Ao final da partida, é mostrado um ranking com as 5 melhores partidas, salvo em `data/ranking.txt`. Em caso de empate na pontuação, a partida com menor tempo fica à frente.

## 10. Controles previstos

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- R (na tela de Game Over): jogar de novo
- ESC (na tela de Game Over): encerrar o jogo

## 11. Organização do código

- `main.py`: ponto de entrada; importa e chama `executar_jogo()`.
- `src/jogo.py`: loop principal, renderização, HUD, campo quadriculado e tela de Game Over.
- `src/config.py`: constantes globais (tamanho da tela, cores, caminhos de arquivos).
- `src/funcoes.py`: funções utilitárias de lógica pura (pontuação, colisão, limites).
- `src/dados.py`: leitura e escrita do ranking em arquivo texto.
- `src/sprites.py`: carregamento e recorte de spritesheet (disponível para uso futuro).

## 12. Recursos externos

Nenhum asset externo está sendo utilizado na versão atual. Todos os gráficos são desenhados
via `pygame.draw` e a fonte utilizada é a fonte de sistema padrão do Pygame.

Caso seja adicionada música de fundo, o arquivo deve ser salvo em `assets/sons/musica.ogg`
e sua origem e licença devem ser registradas no README principal.

## 13. Principais dificuldades esperadas

- Fazer a cobra não inverter a direção de forma errada.
- Garantir que a comida não apareça acima da linha do HUD.
- Organizar o código em funções separadas de forma clara.
- Implementar o ranking com desempate por tempo.

## 14. Escopo mínimo para a entrega final

A versão mínima do jogo terá a cobra se movendo e crescendo ao coletar comida, detecção de
colisão com borda, corpo próprio e linha do HUD, pontuação e tempo exibidos no HUD, ranking
Top 5 salvo em arquivo, tela de Game Over com opção de reiniciar, campo quadriculado verde,
código dividido em módulos e pelo menos 4 testes com pytest.

## 15. Possíveis melhorias, caso haja tempo

- Tela inicial com menu.
- Sons ao coletar comida e ao perder.
- Aumento progressivo de velocidade conforme a pontuação cresce.
- Garantir que a comida nunca apareça sobre o corpo da cobra.   