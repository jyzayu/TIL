#싸피에서도 정렬 풀면서 1차원 배열 가장 큰수와 가장 작은수의 차이가 K이하인것 이어서 정렬했는데  여기서 가장 범위 큰거 작은거 차이 작은거를 구하니까 정렬 
#정렬 알았으면 빨리 풀었을텐데   큰거 그다음 큰거 연속으로 구할때만 바로 생각났었는듯 
def solution(arr, K):
    #여기에 코드를 작성해주세요.
    arr.sort()
    answer = int(1e9)

    for s in range(len(arr) - K):
        answer = min(answer, arr[s + K - 1] - arr[s])

    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [9, 11, 9, 6, 4, 19]
K = 4
ret = solution(arr, K)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
