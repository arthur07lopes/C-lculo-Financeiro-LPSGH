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
  if not result.is_finite():
    raise ValueError("Digite um número válido.")
  if result <0:
    raise ValueError("O valor não pode ser negativo.")
  return normalize(result)

def format_money(value):
  value = normalize(value)
  negative = value < 0
  value = abs(value)
  integer, cents = f"{value:.2f}".split(".")
  parts = []
  while integer:
    parts.insert(0, integer[-3:])
    integer = integer[:-3]
  text = ".".join(parts) + "," + cents
  return f"-{text}" if negative else text

class FinanceManager:
  def __init__(self):
    self.salary = Decimal("0.00")
    self.accounts.clear()

  def add_account(self, name, value, category):
    name = " ".join(name.strip().split())
    category " ".join(category.strip().split()) or "Outros"
    if not name:
      raise ValueError("Digite o nome da conta.")
    self.accounts.append(Account(name, normalize(value), category, False))

  def remove_account(self, index):
    if index < 0 or index >= len(self.accounts):
      raise ValueError("Nenhuma conta válida foi selecionada.")
    del self.accounts[index]

  def toggle_paid(self, index):
    if index < 0 or index >= len(self.accounts):
      raise ValueError("Nenhuma conta válida foi selecionada.")
    self.accounts[index].paid = not self.accounts[index].paid

  def total(self):
    return normalize(sum((item.value for item in self.accounts), Decimal("0.00")))

  def paid_total(self):
    return normalize(sum((item.value for item in self.accounts if item.paid), Decimal("0.00")))

  def pending_total(self):
    return normalize(self.total() - self.paid_total())

  def balance(self):
    return normalize(self.salary - self.total())

  def percentage(self):
    if self.salary <= 0:
      return Decimal("0.00")
    return normalize(self.total * Decimal("100") / self.salary)

  def summary(self):
    return FinancialSummary(
      salary=self.salary,
      total=self.total(),
      paid_total=self.paid_total(),
      pending_total=self.pending_total(),
      balance=self.balance(),
      percentage=self.percentage(),
    )

  def to_dict(self):
    return {
      "salary": str(self.salary),
      "accounts": [account.to_dict() for account in self.accounts],
    }

  def from_dict(self, data):
    self.salary = normalize(Decimal(str(data.get("salary", "0"))))
    self.accounts = [Account.from_dict(item) for item in data.get("accounts", [])]
