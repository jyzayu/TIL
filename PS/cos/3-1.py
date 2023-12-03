#이런 식으로 함수짜서 구현하면 문제가 길 때 도움이 될 수 있겠지.
#.. 전체적인 그림볼때 도움 되겠지..

# zip함수 모름 zip(*iterables) iterable 개수 만큼 길이의
#튜플이  iterable의 i번쨰 원소가 넣어진 튜플이 전달된다.
#shortest argument 가 소진될 때까지

# 같은지 확인할 때 구성성분 같은지 길이 같은지 암기 안 됨
# 문제 글자 그대로 뒤에서 뺴고 앞으로 넣고 할려 했는데
# 2배로 늘린다음 비교하면 한칸 이동하는 연산이 없어 더 빠르겠다.

#3
def func_a(arr):
    ret = arr + arr
    return ret
#2
def func_b(first, second):
    MAX_NUMBER = 1001
    counter = [0 for _ in range(MAX_NUMBER)]
    for f, s in zip(first, second):
        counter[f] += 1
        counter[s] -= 1
    for c in counter:
        if c != 0:
            return False
    return True
#4
def func_c(first, second):
    length = len(second)
    for i in range(length):
        if first[i : i + length] == second:
            return True
    return False

def solution(arrA, arrB):
    if len(arrA) != len(arrB):
        return False
    if func_b(arrA, arrB):
        arrA_temp = func_a(arrA)
        if func_c(arrA_temp, arrB):
            return True
    return False
