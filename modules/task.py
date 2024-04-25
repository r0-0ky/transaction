import re

from findForks import find_forks
from clearTransactions import clear_transactions
from bubbleSort import sort_by_bubble
from selectionSort import sort_by_selection
from parseTransactions import parse_transactions
from linearBlockFinder import get_block_by_index_linear
from binaryBlockFinder import get_block_by_index_binary

transactions = parse_transactions()
selectionSort = sort_by_selection(transactions)
bubbleSort = sort_by_bubble(transactions)
integratedSort = sorted(transactions, key=lambda mas: mas['index'])
clearTransactions = clear_transactions(transactions)
clearSortedTransactions = clear_transactions(bubbleSort)
forks = find_forks(bubbleSort)

def runTransactionQuestions():
  print("Задание 1")
  for i in clearSortedTransactions:
    if re.match(r'.*000$', i['hash']):
      print(f"{i['index']}\n{i['transactions'][-1]['to']}\n")

  print("Задание 2")
  print(min(forks), '\n')

  print("Задание 3")
  print(forks[min(forks)][0]['index'], '\n')

  print("Задание 4")
  print(len(forks[max(forks)]), '\n')

  print("Задание 5")
  print(forks[max(forks)][-1]['hash'], '\n')

  print("Задание 6")
  print(len(forks), '\n')

  print("Задание 7")
  for i in clearSortedTransactions:
    if i['index'] == 71:
      for k in i['transactions']:
        if k['from'] == "SYSTEM":
          print(k['value'],'\n')

  print('Задание 8')
  counter = {}
  for i in clearSortedTransactions:
    for k in i['transactions']:
      if k['from'] == "SYSTEM":
        if i['index'] != 0 and not(k['value'] in counter):
          counter[k['value']] = 0     
        if i['index'] != 0 and len(counter) == 0 or k['value'] in counter:
          counter[k['value']] += 1
  print(counter, '\n')

  print('Задание 9')
  firstBlock = list(counter.keys())[0]
  secondBlock = list(counter.keys())[1]
  coefficient = round( secondBlock / firstBlock, 2)
  print(coefficient, '\n')

  print('Задание 10')
  print(100 + 17 - list(counter.values())[-1] + 17, '\n')
        

  print('Задание 11')
  blocksWithInfo = []
  for i in clearSortedTransactions:
    if i['secret_info'] != '':
      blocksWithInfo.append(i['index'])
  print(blocksWithInfo, '\n')

  print('Задание 12')
  mes = ''
  for i in blocksWithInfo:
    for k in clearSortedTransactions:
      if k['index'] == i:
        mes += k['secret_info']

  print(mes, '\n')

  print('Задание 13')
  bytes_object = bytes.fromhex(mes)
  decoded_string = bytes_object.decode("utf-8")
  print(decoded_string, '\n')

def runSorts():
  print('Линейная сортировка с отсортированным массивом\n')
  get_block_by_index_linear(clearSortedTransactions, 1)
  get_block_by_index_linear(clearSortedTransactions, len(clearSortedTransactions) - 1)
  get_block_by_index_linear(clearSortedTransactions, round(len(clearSortedTransactions) / 2))
  get_block_by_index_linear(clearSortedTransactions, len(clearSortedTransactions) - 21)
  get_block_by_index_linear(clearSortedTransactions, 21121)

  print('Линейная сортировка с неотсортированным массивом\n')
  get_block_by_index_linear(clearTransactions, 1)
  get_block_by_index_linear(clearTransactions, len(clearTransactions) - 1)
  get_block_by_index_linear(clearTransactions, round(len(clearTransactions) / 2))
  get_block_by_index_linear(clearTransactions, len(clearTransactions) - 21)
  get_block_by_index_linear(clearTransactions, 21121)

  print('Бинарная сортировка с отсортированным массивом\n')
  get_block_by_index_binary(clearSortedTransactions, 1)
  get_block_by_index_binary(clearSortedTransactions, len(clearSortedTransactions) - 1)
  get_block_by_index_binary(clearSortedTransactions, round(len(clearSortedTransactions) / 2))
  get_block_by_index_binary(clearSortedTransactions, len(clearSortedTransactions) - 21)
  get_block_by_index_binary(clearSortedTransactions, 21121)