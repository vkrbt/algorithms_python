def find_solution(positions, costs):
  solution = [0, costs[0]]
  for i in range(2, len(positions)):
    solution.append(max(solution[i - 1], costs[i] + solution[get_nearest_cost(positions, i)]))
  return solution

def get_nearest_cost(positions, pos):
  current = positions[pos]
  pos = pos - 1  
  while current - positions[pos] < 5:
    pos = pos - 1
  return pos
