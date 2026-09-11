from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Account:
  name: str
  value: Decimal
  category: str = "Outros"
  paid: bool = False

  def to_dict(self):
    return {
      "name": self.name,
      "value": str(self.value),
      "category": self.category,
      "paid": self.paid,
    }

  @classmethod
  def from_dict(cls, data):
    return cls(
      name=str(data.get("name", "")).strip(),
      value=Decimal(str(data.get("value", "0"))),
      category=str(data.get("category", "Outros")).strip or "Outros",
      paid=bool(data.get("paid", False)),
    )

  def display(self, index):
    state = "paga" if self.paid else "pendente"
    return f"{index}. {self.name} | {self.category} | R$ {self.value:.2f} | {state}"

@dataclass
class FinancialSummary:
  salary: Decimal
  total: Decimal
  paid_total: Decimal
  pending_total: Decimal
  balance: Decimal
  percentage: Decimal
