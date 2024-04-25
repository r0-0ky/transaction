def clear_transactions(arr):
  clearTransactions = []
  for x in arr:
    isFinded = False
    for trans in clearTransactions:
      if (trans['index'] == x['index']):
        isFinded = True
    if (not isFinded):
      clearTransactions.append(x)
  return clearTransactions