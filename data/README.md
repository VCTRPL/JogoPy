# Dados

Esta pasta guarda arquivos de persistência simples em texto.

## Arquivos

- `ranking.txt`: armazena as 5 melhores partidas no formato `pontos;tempo` por linha,
  ordenadas da maior para a menor pontuação. Criado automaticamente ao final da primeira
  partida.

## Formato do ranking.txt

```
34;96
8;23
6;17
```

Cada linha representa uma entrada: pontuação e tempo em segundos separados por `;`.

## Observação

Evite editar o arquivo manualmente. Se o arquivo estiver corrompido (formato incorreto),
apague-o — o jogo criará um novo automaticamente.
