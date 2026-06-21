# Testes

Esta pasta contém os testes automatizados do projeto Snakobra,
cobrindo a lógica pura de `src/funcoes.py` e as regras de ranking de `src/dados.py`.

## Arquivos

- `test_logica.py`: testes das funções de lógica do jogo e do sistema de ranking.

## Como executar

Na raiz do projeto (`JogoPy/`), rode:

```bash
python -m pytest
```

Para ver o resultado de cada teste individualmente:

```bash
python -m pytest -v
```

## Casos de teste

### `calcular_pontos` — soma de pontuação

| Teste | Descrição |
|---|---|
| `test_calcular_pontos` | Verifica que pontos atuais e pontos ganhos são somados corretamente. |

### `jogador_perdeu` — condição de derrota

| Teste | Descrição |
|---|---|
| `test_jogador_perdeu_com_zero_vidas` | Retorna `True` quando o jogador chega a 0 vidas. |
| `test_jogador_nao_perdeu_com_vidas` | Retorna `False` enquanto o jogador ainda tem vidas restantes. |

### `limitar_valor` — clamp de valores

| Teste | Descrição |
|---|---|
| `test_limitar_valor_abaixo_do_minimo` | Retorna o mínimo quando o valor está abaixo do intervalo. |
| `test_limitar_valor_acima_do_maximo` | Retorna o máximo quando o valor está acima do intervalo. |
| `test_limitar_valor_dentro_do_intervalo` | Mantém o valor original quando já está dentro do intervalo. |

### `atualizar_ranking` — regras do ranking

| Teste | Descrição |
|---|---|
| `test_ranking_insere_e_ordena_por_pontos` | A maior pontuação deve aparecer no topo do ranking após a inserção. |
| `test_ranking_respeita_limite` | Quando o ranking está cheio, pontuações menores que o último colocado não entram. |
| `test_ranking_desempata_pelo_menor_tempo` | Em caso de empate na pontuação, quem completou em menos tempo fica à frente. |

