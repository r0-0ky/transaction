def find_forks(sortedArr):
  res = {}
  count = 0
  arr = []
  for i in sortedArr:
    if sortedArr.index(i) != len(sortedArr) - 1:
      if sortedArr[sortedArr.index(i) + 1]['index'] == i['index']:
        count += 1
        arr.append({"index": i['index'], "hash": i['hash']})
      elif sortedArr.index(i) != len(sortedArr) - 2 and sortedArr[sortedArr.index(i) + 1]['index'] != sortedArr[sortedArr.index(i) + 2]['index']:
        if count != 0:
          res[count] = arr
        count = 0
        arr = []
    else:
      if count != 0:
        res[count] = arr
  return res