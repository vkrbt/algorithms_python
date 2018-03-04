def find_solution(costs):
  max_cost = [costs[0], costs[1]]
  max_pos = [[0], [1]]
  for i in range(2, len(costs)):
    new_max = costs[i] + max_cost[i - 2]
    prev_max = max_cost[i - 1]
    if new_max > prev_max:
      max_cost.append(new_max)
      new_max_pos = max_pos[i - 2][:]
      new_max_pos.append(i)
      max_pos.append(new_max_pos)
    else:
      max_cost.append(prev_max)
      max_pos.append(max_pos[i - 1][:])
  return {'cost': max_cost[-1], 'positions': max_pos[-1]}
