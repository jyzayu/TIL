from collections import deque


#방문 했던 곳을 다른 방법으로 갔을 때 더 빠를 수 있지 않나? 
# 큐로 bfs로 구현하면 더 빨리 가는 곳이 가서 먼저 visit하기 때문에 그건 아님
# 그리고 모두하기는 하지만 target 범위를 확인하여 n이 범위 넘어가면 안 됨
# 더 하는 건 상한   뺴는건 하한 안 넘어가는지 

#거리를 cnt가 아닌 visited 에 기록한다 현재 위치에서 +1 씩 해가면서
#방문 안 한곳을 0으로 하기 위해 시작위치를 1로 시작해서 연산횟수 1더하다가 
#마지막에 구한 연산횟수 -1 , 1에서 부터 시작했으니까 

def solution(number, target):
    #여기에 코드를 작성해주세요.
    answer = int(1e9)
    visited = [0] * 10001
    def bfs():
        q = deque()
        q.append(number)
        visited[number] = 1

        while q:
            x = q.popleft()
            if x == target:
                break
            if x + 1 < 10001 and visited[x + 1] == 0:
                q.append(x + 1)
                visited[x + 1] = visited[x] + 1
            if x - 1 >= 0 and visited[x - 1] == 0:
                q.append(x - 1)
                visited[x - 1] = visited[x] + 1
            if x * 2 < 10001 and visited[x * 2] == 0:
                q.append(x * 2)
                visited[x * 2] = visited[x] + 1

    bfs()
    return visited[target] - 1
