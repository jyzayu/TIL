# 답지 없음
def solution(K, words):
    left = K
    line = ""
    cnt = 1
    i = 0

    

    while i < len(words):
        # left 에  words[i]를 넣을 수 있다면 (left가 크거나 같다면)
        # 다음 words를 넣는다 i + 1 
        if left >= len(words[i]):
            line += words[i]
            line += "_"
            left -= (len(words[i]) + 1)
            i += 1

        # 한 줄의 끝에 단어 하나를 완전히 적지 못한다면, 
        # 그 줄의 나머지 부분을 모두 공백으로 채우고 
        else:
            for _ in range(left):
                line += "_"
            line = ""
            cnt += 1
            left = K
    return cnt
        # 다음 반복문 부터 다시 단어를 적어야함 
        # => for 아닌 while로 앞에서 부터 하나씩
        # => line = "", left = K 초기화, cnt + 1


#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
K = 10
words = ["nice", "happy", "hello", "world", "hi"]
ret = solution(10, words)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
