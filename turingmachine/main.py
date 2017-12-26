def prepare(num):
  num = 'a' + num + 'b' * (len(num) + 2)
  num = list(num)
  index = 0;
  while num[index] is not 'b':
    index += 1
  index -= 1
  state = num[index]
  num[index] = '_'
  while num[index] is not 'b':
    index += 1
  num[index] = state
  return num


def invert_number(num):
  num = prepare(num)
  index = 0
  while num[index] is not '_':
    index += 1
  index -= 1
  state = num[index]
  while num[index] is not 'a':
    num[index] = '_'
    while num[index] is not 'b':
      index += 1
    num[index] = state
    while num[index] is '1' or num[index] is '0':
      index -= 1
    while num[index] is '_':
      index -= 1
    state = num[index]
  index += 1
  while num[index] is '_':
    num[index] = 'a'
    index += 1
  return ''.join(num)


if __name__ == '__main__':
  num = '1001011101'
  print(invert_number(num));