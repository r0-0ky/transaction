def sort_by_bubble(arr):
  newArr = arr.copy()
  n = len(newArr)
  for i in range(n):
    for j in range(n - i - 1):
      if (newArr[j]['index'] > newArr[j + 1]['index']):
        temp = newArr[j + 1]
        newArr[j + 1] = newArr[j]
        newArr[j] = temp
  return newArr