from pathlib import Path

APP_NAME = "LGHS Finanças"
APP_VERSION = "1.0"
WINDOW_SIZE = (1240, 850)
MIN_SIZE = (1020, 720)

# Paleta de cores 
BLUE = (0, 125, 184)
BLUE_DARK = (0, 90, 138)
NAVY = (0, 61, 92)
NAVY_2 = (0, 46, 71)
WHITE = (255, 255, 255)
BG = (247, 249, 251)
TEXT = (34, 34, 34)
MUTED = (95, 103, 110)
BORDER = (221, 228, 235)
GREEN = (18, 116, 69)
GREEN_BG = (231, 247, 237)
RED = (176, 39, 39)
RED_BG = (252, 236, 236)
YELLOW = (126, 96, 0)
YELLOW_BG = (255, 248, 222)

CATEGORIES = (
  "Moradia",
  "Alimentação",
  "Transporte",
  "Educação",
  "Saúde",
  "Internet e Telefone",
  "Lazer",
  "Outros",
)

SHORTCUTS = (
  ("F1", "Abrir ajuda e acessibilidade"),
  ("F3", "Atualizar cálculo"),
  ("F4", "Ir para o cadastro de conta"),
  ("F6", "Remover conta selecionada"),
  ("F7", "Marcar ou desmarcar com paga"),
  ("Ctrl+N", "Nova análise"),
  ("Ctrl+S", "Salvar análise"),
  ("Ctrl+O", "Carregar Análise"),
  ("Ctrl+E", "Exportar CSV"),
  ("Ctrl+Q", "Sair"),
)

DATA_DIR = Path.home() / "lpsgh_financas"
JSON_FILE = DATA_DIR / "análise.json"
CSV_FILE = DATA_DIR / "contas.csv"
