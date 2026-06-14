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

Na tela aparece uma cobra e um item de comida em posição aleatória. O jogador controla a direção da cobra usando as setas do teclado. O objetivo é coletar os itens de comida, fazendo a cobra crescer e a pontuação aumentar. O desafio é evitar colidir com as bordas da tela ou com o próprio corpo da cobra, que fica maior a cada item coletado.

## 5. Objetivo do jogador

Coletar o maior número possível de itens de comida, fazendo a cobra crescer e acumulando a maior pontuação possível.

## 6. Regras principais

- A cobra se move continuamente na direção atual, sem parar.
- O jogador muda a direção usando as setas do teclado.
- Não é possível inverter a direção diretamente (ex.: ir para cima enquanto está se movendo para baixo).
- Cada item de comida coletado vale 10 pontos e faz a cobra crescer.
- A comida reaparece em posição aleatória após ser coletada, nunca sobre o corpo da cobra.

## 7. Condição de vitória

Conseguir preencher todo o espaço da tela com a cobra. O objetivo é sobreviver o máximo possível e alcançar a maior pontuação.

## 8. Condição de derrota ou encerramento

A partida termina quando a cobra colide com a borda da tela, com o próprio corpo ou termina de preencher toda a tela. O jogador também pode encerrar manualmente pressionando ESC ou fechando a janela.

## 9. Elementos previstos no jogo

### Jogador ou elemento principal

A cobra, representada por uma lista de posições que formam seu corpo. É controlada pelas setas do teclado e cresce ao coletar comida.

### Obstáculos, inimigos ou desafios

O próprio corpo da cobra e as bordas da tela funcionam como obstáculos. À medida que a cobra cresce, desviar do próprio corpo se torna progressivamente mais difícil.

### Itens, alvos ou objetos de interação

Itens de comida que aparecem em posição aleatória na tela. Ao ser coletado, o item some e reaparece em outro lugar, nunca sobre o corpo da cobra.

### Pontuação, vidas, tempo ou progresso

A pontuação é exibida na tela e aumenta 10 pontos a cada item coletado. O recorde é salvo em um arquivo `record.txt` e exibido ao jogador.

## 10. Controles previstos

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- ESC: encerrar o jogo

## 11. Organização inicial do código

O código será dividido em funções separadas de forma clara. A organização planejada é:
> - `main.py`: inicia o jogo e contém o loop principal;
> - `src/config.py`: guarda configurações como tamanho da tela, velocidade e cores (usando dicionário);
> - `src/cobra.py`: contém funções relacionadas à cobra (movimento, crescimento, colisão);
> - `src/comida.py`: contém funções relacionadas à geração e coleta da comida;
> - `src/arquivos.py`: contém funções de leitura e escrita do arquivo de recorde (`record.txt`).

## 12. Recursos externos previstos

Não pretendemos utilizar recursos externos.

## 13. Principais dificuldades esperadas

- Fazer a cobra não inverter a direção de forma errada.
- Garantir que a comida não apareça em cima do corpo da cobra.
- Organizar o código em funções separadas de forma clara.

## 14. Escopo mínimo para a entrega final

A versão mínima do jogo terá a cobra se movendo e crescendo ao coletar comida, detecção de colisão com borda e corpo próprio, pontuação exibida na tela, salvamento do recorde em arquivo, tela de game over com opção de reiniciar, código dividido em funções e pelo menos 4 testes com pytest.

## 15. Possíveis melhorias, caso haja tempo

- Tela inicial com menu.
- Sons ao coletar comida e ao perder.
- Aumento progressivo de velocidade conforme a pontuação cresce.