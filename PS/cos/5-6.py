#저번에 반복문으로 하고 시간초과난거 함수사용하니 통과하길래 그 떄 외웠었다.  oct는 기억이 안났는데 oct가 octa 나타내는 거였군..
def solution(s1, s2, p, q):
    return oct(int(s1, p) + int(s2, p))[2:]

#반복문이 아니라 재귀로 해서 10진수 => q진수로 변환했네 
#각 자리 수를 끝에서 부터 1부터 p씩 곱해진 수를 계속 곱해서 더한다.  notational 표기 

numbers_int = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def char_to_int(ch):
    for i in range(10):
        if ch == numbers_char[i]:
            return numbers_int[i]

def int_to_char(val):
    for i in range(10):
        if val == numbers_int[i]:
            return numbers_char[i]

def convert_scale(num, q):
    if num == 0:
        return ""
    return convert_scale(num // q, q) + int_to_char(num % q)

def parse_decimal(s, p):
    num = 0
    mul = 1
    for s_i in reversed(s):
        num += char_to_int(s_i) * mul
        mul *= p
    return num

def solution(s1, s2, p, q):
    num1 = parse_decimal(s1, p)
    num2 = parse_decimal(s2, p)
    answer = convert_scale(num1 + num2, q)
    return answer
