import json
from advertising import find_solution

if __name__ == '__main__':
  data = json.load(open('./dynamic_programming/advertising_problem/data.json'))
  print(find_solution(data['positions'], data['costs'], 5))
