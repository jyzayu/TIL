def solution(n, garden):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    nxt_garden = garden1.copy()
    
    day = 0
    while True:
        #1일 지나고서 모든 꽃이 폈는지
        zero = 0 # 0 cnt
        for i in range(n):
            zero += garden[i].count(0)
        if zero == 0:
            return day
        
    # 1일 동안 꽃 피우는거 반영
        for i in range(n):
            for j in range(n):
                if garden[i][j] == 1:
                    # 상하좌우 nxt 1로 바꾸기
                    for k in range(4):
                        nr = i + dr[k]
                        nc = j + dc[k]
                        if 0 <= nr < n and 0 <= nc < n:
                            nxt_garden[nr][nc] = 1
    #1일 지났으니 day + 1
        day += 1

      
import queue

def solution(n, garden):
    answer = 0

    q = queue.Queue()
    dx = [ -1, 1, 0, 0 ]
    dy = [ 0, 0, -1, 1 ]

    for i in range(n) :
    	for j in range(n) :
    		if garden[i][j] == 1 :
    			q.put((i, j, 0))

    while q.empty() == False :
    	x, y, day = q.get()

    	for i in range(4) :
    		next_x = x + dx[i]
    		next_y = y + dy[i]
    		next_day = day + 1

    		if (0 <= next_x and next_x < n and 0 <= next_y and next_y < n) and (garden[next_x][next_y] == 0) :
    			garden[next_x][next_y] = 1
    			answer = next_day
    			q.put((next_x, next_y, next_day))

    return answer
