
# while 에서 if 에서만 +1이 아닌 else 에서 +1도 정의해야함
#왜 정렬해야만 했을까?
# a [ 2, 4, 2]
# e [ 6 5 4 3 2 1]        
 # e 가 더 크니까 e를 계속 증가시키면서 바꿨음 근데 지나간 곳에서 
#a랑 매치하는 e가 앞에 있을 수 있음 그래서
#작은거는 작은거 끼리 순차적으로 매칭시켜야함 대충 이렇지 안흥ㄹ까 


#  2가 idx 4 부터 매칭하네  a= 0인데  그래 매치해서 다음꺼보니까 a 값이 4네 
# e idx 5부터 작은거만 있네 다시 e를 완탐해야지만 매칭하는걸 찾잖아 
# 그니까 가장 작은거  2번째로 작은거 3번쨰로 작은거 가장 작은거를 연속으로 찾으니까  정렬하면 좋다.

def solution(enemies, armies):
    #여기에 코드를 작성해주세요.
    armies.sort()
    enemies.sort()

    i = 0
    j = 0
    while i < len(enemies) and j < len(armies):
        if enemies[i] <= armies[j]:
            i += 1
            j += 1
        else:
            j += 1

    return j

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
enemies1 = [1, 4, 3]
armies1 = [1, 3]
ret1 = solution(enemies1, armies1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

enemies2 = [1, 1, 1]
armies2 = [1, 2, 3, 4]
ret2 = solution(enemies2, armies2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
