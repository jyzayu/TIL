#각 자리수 구하는거 cos pro에서 자주 본다
#수업 듣길 잘 했네..
# %로 끝 자리 구하고 
# //로 끝 자리 1개 지우고  0이 될떄까지 반복..
def power(base, exponent):
    val = 1
    for i in range(exponent):
        val *= base
    return val

def solution(k):
    answer = []
    bound = power(10, k)
    for i in range(bound // 10, bound):
        current = i
        calculated = 0
        while current != 0:
            calculated += power(current % 10, k)
            current //= 10
        if calculated == i:
            answer.append(i)
    return answer
