#deque으로 구현한다음  i+1이 홀수일 때 뒤집지 않고 짝수일때 뒤집고
#그렇게 한 번만 뒤집는걸 생각했는데, 앞뒤로 넣으면서 
#그리고 q에 있는 원소들이 str들 이니까 
#''.join으로 ? 하면 될듯

#::-1만 알면 되는 거였다.
def solution(n):
    answer = ''
    for i in range(n):
        answer += str(i + 1)
        answer = answer[::-1]
    return answer
