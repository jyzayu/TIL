#나는 재사용하려는게 아니니까 2-1 2 같이 한 줄 단위로 작성할 필요는 없을 것 같고
#2-1 1, 이나 345 합쳐서 하나로 한 것처럼 추상화해서  한번에 볼수있는 코드를 늘리면 내가 전체적으로 이해하는데 편할 것 같은데 ? 

#2-1 2
def func_a(arr, s):
    return s in arr
#2-1 1
def func_b(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return False
    return True
#345
def func_c(palindromes, k):
    palindromes = sorted(palindromes)
    if len(palindromes) < k:
        return "NULL"
    else:
        return palindromes[k - 1]

def solution(s, k):
    palindromes = []
    length = len(s)
    #이 길이를 어떻게 설정할지 생각하지 못했는데 

    #startIdx에서 길이가 1인 문자열 부터 문자열 끝까지? 
    # for문에서 length -start_idx + 1? 이면 값 넣으면
    # [:length] s[length-1]까지 가니까 idxError X

    #아 반복문도 끝-1까지 들어가고   
    #:도 -1까지 들어가는거 해깔리네 ; 전에 문제풀 때도 이런거
    #여러개 같이 쓰이면 해깔리던데 ㅜㅠ
    #배열에는 0번쨰부터 쓰지만 문제에선 0번쨰를 1번쨰로 쓰고
    #1번쨰 값을 가지고 2번쨰 예측값을 구한다 이런식
    for start_idx in range(length):
        for cnt in range(1, length - start_idx + 1):
            sub_s = s[start_idx : start_idx + cnt]
            if func_b(sub_s) == True:
                if func_a(palindromes, sub_s) == False:
                    palindromes.append(sub_s)

    answer = func_c(palindromes, k)
    return answer
