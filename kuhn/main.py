def dfs(v, matching, used, graph):
  if (used[v]):
    return False

  used[v] = True

  for to in graph[v]:
    if (matching[to] == -1 or dfs(matching[to], matching, used, graph)):
      matching[to] = v
      return True
  return False

def fill(size, value):
  return [value for i in range(0, size)]

if __name__ == '__main__':
  graph = [[4],
           [5],
           [1, 4],
           [4],
           [0, 3],
           [1]]
  N = len(graph)
  used = []
  matching = []
  matching = fill(N, -1)
  for i in range(0, N):
    used = fill(N, False)
    dfs(i, matching, used, graph)

  for i in range(0, N):
    if matching[i] != -1:
      print(i, matching[i])

# http://kvodo.ru/adjacency-list.html