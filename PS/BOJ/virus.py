#list는 global scope를 갖는다. 

# 연결된 노드 그래프를 표현하는 list
#인접리스트 or 인접행렬 
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
cnt = 0
for i in range(m):
  a, b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(v):
  global cnt
  cnt += 1
  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      # visit and append
      dfs(i)
  return cnt
print(dfs(1) -1)
