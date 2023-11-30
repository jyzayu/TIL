# 전체에서 개수가 아닌 연속해서 나오는 것의 수이므로  앞에꺼랑 계속 비교해야함 
# 마지막에 끝날 때 다른것이 나오고 끝나든 같은것이 나온채 끝나든  answer에 더하지 않았으니 마지막에 한 번 더 

def solution(s):
    s = s.lower()
    answer = ""
    previous = s[0]
    counter = 1
    for alphabet in s[1:]:
        if alphabet == previous:
            counter += 1
        else:
            answer += previous + str(counter)
            counter = 1
            previous = alphabet
    answer += previous + str(counter)
    return answer
