import json
from pathlib import Path

def parse_transactions():
  directory = Path('transactions')
  transactions = []
  for filepath in directory.iterdir():
    if filepath.is_file():
      with open(filepath, 'r') as file:
        transactions.append(json.load(file))
  return transactions