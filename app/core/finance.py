from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

from app.core.models import Account, FinancialSummary

CENT = Decimal("0.01")


def normalize(value):
  return value.quantize(CENT, rounding=ROUND_HALF_UP)


def parse_money(text):
  value = text.strip().upper().replace("R$", "").replace(" ", "")
  if not value:
    raise ValueError("Digite um valor.")
  if "," in value:
    value = value.replace(".", "").replace(",", ".")
  try:
    result = Decimal(value)
  except InvalidOperation as error:
    raise ValueError("Valor inválido. Exemplo: 1250,50.") from error
