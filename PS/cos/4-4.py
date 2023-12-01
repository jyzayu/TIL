#문제 1번 다 읽고 나서 풀기
# 0 의 위치, 없는 수를 찾기 위해 2차 반복문 
# [i,j]를 list 에 append

# 있는 것들을 True로 기록할 정사각형 크기만큼의 1차원 배열
# exist != True면 그것이 없는 수 


# 각 함수가 의미하는 것 
#각 코드가 의미하는 것 작성하면서 하기 

# 2 없는 수 2개 찾기
def func_a(matrix):
    n = 4
    ret = []
    # 
    exist = [False for _ in range(n*n + 1)]
    for i in range(0, n):
        for j in range(0, n):
                exist[matrix[i][j]] = True
    for i in range(1, n*n+1):
        if exist[i] == False:
            ret.append(i)
    return ret
# 1 두 빈칸 위치 찾기
def func_b(matrix):
    n = 4
    ret = []
    for i in range(0, n):
        for j in range(0, n):
            if matrix[i][j] == 0:
                ret.append([i, j])
    return ret
#마방진인지 확인
def func_c(matrix):
    n = 4
    goal_sum = sum(range(1, n*n+1))//n
    for i in range(0, n):
        row_sum = 0
        col_sum = 0
        for j in range(0, n):
            row_sum += matrix[i][j]
            col_sum += matrix[j][i]
        if row_sum != goal_sum or col_sum != goal_sum:
            return False

    main_diagonal_sum = 0
    skew_diagonal_sum = 0
    for i in range(0, n):
        main_diagonal_sum += matrix[i][i]
        skew_diagonal_sum += matrix[i][n-1-i]
    if main_diagonal_sum != goal_sum or skew_diagonal_sum != goal_sum:
        return False
    return True
