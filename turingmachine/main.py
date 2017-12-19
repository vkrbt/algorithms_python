def prepare(num):
  num = list(num);
  last_pos = num.index('b') - 1
  last_state = num[last_pos]
  num[last_pos] = '_';
  num[last_pos + 1] = last_state
  return num


def invert_number(num):
  num = prepare(num)
  while num[num.index('_') - 1] is not 'a':
    last_pos = num.index('_') - 1
    last_state = num[last_pos]
    num[num.index('b')] = last_state
    num[last_pos + 1] = 'a'
    num[last_pos] = '_'
  num[last_pos] = 'a'
  return ''.join(num)


if __name__ == '__main__':
  num = 'a1001011101bbbbbbbbbbbbbbbbbbbbbb'
  print(invert_number(num));