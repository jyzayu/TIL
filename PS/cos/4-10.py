import math

# 에라토스테네스   그냥 소수 구하는거 많이 해야될 떄니까 발상이 쉽네  그래도 늘긴 하는구나
def solution(a, b):
    # 여기에 코드를 작성해주세요.
    #b//2 까지의 소수를 모두 구한다? 에라토스테네스?
    #2, 3 각 수(isPrime=false인 것 중 가장 작은수) 의 *2부터 b//2까지 배수를 모두 지운다. 
    # isPrime[i] = false
    n = b // 2
    # n = int(math.sqrt(b)) 를  n**2 하면 25가 나온다  (b가 30일떄)  그 이상의 소수는 구해봤자 b를 넘어가니 구할 필요 없다. 
    #그러므로  int(sqrt(b)) 까지만 소수를 구하면 된다.
    answer = 0

    isPrime = [True] * (n + 1)
    isPrime[1] = False
    for i in range(2, n + 1):
        if isPrime[i] == True:
            #배수를 *2 부터하는건 i+i를  n+1까지 i씩 더하면 된다  곱하기를 더하기의 반복으로 표현 
            #j = 2
            #while i * j < n + 1:
            #j += 1
            for j in range(i+i, n + 1, i):
                isPrime[i * j] = False

    
    print(isPrime)
#2 3 5 7 11 13
    #isPrime == True인 것들을 모두 소수 리스트에 

    for i in range(2, n + 1):
        if isPrime[i] == True:
            if a <= pow(i, 2) <= b:
                answer += 1
            if a <= pow(i, 3) <= b:
                answer += 1
    #그리고 그 소수들을 모두 제곱 세제곱해서 범위에 속하는지 확인? a < b
    return answer
