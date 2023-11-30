#programmers에서 봤던문제 그대로라 보자마자 dfs완탐이 떠올랐다.   
# 인접노드를 AEIOU로 설정 길이가 5일 떄만 추가하는 것이 아닌  
#dfs 호출할때마다 ans에 계속 append한다. 
# word가 들어있는 ans의 idx를 구한다. 

words = []

def create_words(lev, s):
    global words
    VOWELS = ['A', 'E', 'I', 'O', 'U']
    words.append(s)
    for i in range(0, 5):
        if lev < 5:
            create_words(lev + 1, s + VOWELS[i])

def solution(word):
    global words
    words = []
    answer = 0
    create_words(0, '')
    for idx, i in enumerate(words):
        if word == i:
            answer = idx
            break
    return answer
