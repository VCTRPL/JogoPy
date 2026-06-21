# Código-fonte (`src`)

Esta pasta contém os módulos principais do jogo.

## Arquivos

- `jogo.py`: loop principal, eventos, renderização, campo quadriculado, HUD e tela de Game Over.
- `config.py`: constantes globais (tamanho da tela, cores, caminhos de arquivos, FPS).
- `funcoes.py`: funções utilitárias de lógica pura (pontuação, vidas, limites, colisão).
- `dados.py`: leitura e gravação do ranking em arquivo texto (`data/ranking.txt`).
- `sprites.py`: carregamento e recorte de spritesheet BMP (disponível para uso futuro).
- `__init__.py`: marca `src` como pacote Python, permitindo imports do tipo `from src.jogo import ...`.

## Dica de evolução

Quando o projeto crescer, mantenha módulos pequenos e separados por responsabilidade.