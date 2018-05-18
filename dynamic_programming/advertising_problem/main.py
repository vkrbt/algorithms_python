import json
from advertising import find_solution

if __name__ == '__main__':
  data = json.load(open('./dynamic_programming/advertising_problem/data.json'))
  solution = find_solution(data['positions'], data['costs'], 5)
  print(solution)
  f = open('./dynamic_programming/advertising_problem/result.json', 'w')
  f.write(json.dumps(solution, sort_keys=True, indent=2))
