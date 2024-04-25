def sort_by_selection(arr):
  newArr = arr.copy()
  n = len(newArr)
  for i in range(n - 1):
    j = i + 1
    while j < n:
      if newArr[i]['index'] > newArr[j]['index']:
        temp = newArr[i]
        newArr[i] = newArr[j]
        newArr[j] = temp
      j += 1
  return newArr
