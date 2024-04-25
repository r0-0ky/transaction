def get_block_by_index_linear(blocks, num):
  print('Вычесляем линейно...')
  counter = 0
  for block in blocks:
    counter += 1
    isFinded = False
    if block['index'] == num:
      isFinded = True
      break
  if (isFinded):
    print(f'Блок №{num} найден 🟢\nКоличетсво итераций: {counter}\n')
  else:
    print(f'Блок №{num} не найден 🔴\n')
    