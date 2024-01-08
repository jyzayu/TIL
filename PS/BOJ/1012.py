# dfs 를 graph와 dfs 호출 사이에 정의해야한다. 맨 아래에 하면 dfs 를 정의하기 전에 호출해버리고 
#맨 위에 하면 graph가 정의되지 않음

#cnt 를 세고 테스트케이스마다 answer list에 append해뒀다가 나중에 print

#2d array에서 dfs할 때 범위 벗어났는지 확인 안 해서 dfs호출할 때 IndexError 
import sys
sys.setrecursionlimit(10**6)

# dfs할 떄 sys.setrecursionlimit(10**6) RecursionError
T = int(input())

answer = []
for _ in range(T):
  M, N, K = map(int,input().split())
  graph = [[0] * (M) for _ in range(N)]

  dr = [-1, 1, 0 ,0]
  dc = [0, 0, -1, 1]
  def dfs(r, c):
    for i in range(4):
      nr = r + dr[i]
      nc = c + dc[i]
      if 0 <= nr < N and 0 <= nc < M:
        if graph[nr][nc] == 1:
          # visit and append
          graph[nr][nc] = -1
          dfs(nr, nc)
  cnt = 0
  for _ in range(K):
    c, r = map(int,input().split())
    graph[r][c] = 1
  for i in range(N):
    for j in range(M):
      if graph[i][j] == 1:
        dfs(i, j)
        cnt += 1
  answer.append(cnt)
for ans in answer:
  print(ans)




    
