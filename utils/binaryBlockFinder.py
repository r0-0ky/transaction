def get_block_by_index_binary(blocks, num):
  print('Вычесляем бинарно...')
  l = 0
  r = len(blocks)
  counter = 0
  while l + 1 < r:
    counter += 1
    m = (l + r) / 2
    if blocks[int(m)]['index'] <= num:
      l = blocks[int(m)]['index']
    else:
      r = blocks[int(m)]['index']
  if l == num:
    print(f"Блок №{num} найден 🟢")
    print(f'Колличество итераций: {counter} \n')
  else:
    print(f"Блок №{num} не найден 🔴 \n")