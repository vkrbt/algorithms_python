states = dict(
  line_end = '}',
  line_start = '{',
  nums = ['0', '1'],
  empty = '',
)

def invert_number(num):
  num = list(states['line_start'] + num + states['line_end'] * (len(num) + 2))

  index = 0

  while num[index] is not states['line_end']:
    index += 1
  index -= 1
  state = num[index]
  num[index] = states['empty']
  while num[index] is not states['line_end']:
    index += 1
  num[index] = state

  while num[index] is states['empty']:
    index -= 1
  state = num[index]

  while state is not states['line_start']:
    num[index] = states['empty']
    while num[index] is not states['line_end']:
      index += 1
    num[index] = state
    while num[index] in states['nums']:
      index -= 1
    while num[index] is states['empty']:
      index -= 1
    state = num[index]
  index += 1
  while num[index] is states['empty']:
    num[index] = states['line_start']
    index += 1
  while states['line_start'] in num:
    num.remove(states['line_start'])
  return ''.join(num)[:-1]


if __name__ == '__main__':
  num = '1001011100101101'
  num_reversed = ''.join(reversed(list(num)))
  num_reversed_turing = invert_number(num)
  print(num_reversed)
  print(num_reversed_turing)
  print('Right' if num_reversed == num_reversed_turing else 'Wrong')