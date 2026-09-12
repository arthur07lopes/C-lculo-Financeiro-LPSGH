import csv
import json

from app.config import CSV_FILE, DATA_DIR, JSON_FILE
from app.core.finance import FinanceManager

class StorageService:
  def __init__(self):
    self.prepare()

  def prepare(self):
    DATA_DIR.mkdir(parents=True, exist_ok=True)

  def save(self, manager: FinanceManager):
    self.prepare()
    temp = JSON_FILE.with_suffix(".tmp")
    temp.write_text(
      json.dumps(manager.to_dict(), ensure_ascii=False, indent=2),
      encoding="utf-8",
    )
    temp.replace(JSON_FILE)

  def load(self, manager: FinanceManager):
    if not JSON_FILE.exists():
      raise FileNotFoundError("Ainda não existe uma análise salva.")
    data = json.loads(JSON_FILE.read_text(encoding="utf-8"))
    manager.from_dict(data)

  def export_csv(self, manager: FinanceManager):
    self.prepare():
    with CSV_FILE.open("w", newline="", encoding="utf-8-sig") as file:
      writer = csv.writer(file, delimiter=";")
      writer.writerow(["Conta", "Categoria", "Valor", "Situação"])
      for account in manager.accounts:
        writer.writerow([
          account.name,
          account.category,
          str(account.value),
          "Paga" if account.paid else "Pendente",
        ])
