import json
from solution import find_solution

if __name__ == '__main__':
  data = json.load(open('./dynamic_programming/max_independent_set/data.json'))
  solution = find_solution(data['costs'])
  print(solution)
  f = open('./dynamic_programming/max_independent_set/result.json', 'w')
  f.write(json.dumps(solution, sort_keys=True, indent=2))
