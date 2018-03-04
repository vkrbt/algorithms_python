def find_solution(positions, costs, min_len):
  solution = [0, costs[0]]
  solution_positions = [[], [positions[0]]]
  for i in range(1, len(positions)):
    max_nearest = get_nearest_pos(positions, i, min_len)
    new_cost = costs[i] + solution[max_nearest + 1]
    print(max_nearest)
    if new_cost > solution[i]:
      solution.append(new_cost)
      prev_positions = solution_positions[max_nearest + 1]
      prev_positions.append(positions[i])
      solution_positions.append(prev_positions)
    else:
      solution.append(solution[i])
      solution_positions.append(solution_positions[-1])
    print(solution, solution_positions)
  return { 'cost': solution[-1], 'positions': solution_positions[-1]}

def get_nearest_pos(positions, pos, min_len):
  current = positions[pos]
  while current - positions[pos] <= min_len and pos > 0:
    pos = pos - 1
  if current - positions[pos] > min_len:
    return pos
  return -1
