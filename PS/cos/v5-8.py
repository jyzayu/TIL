#최대 공약수 만드는거 이해 안 감

# b 에    a 를 b로 나눴을 떄 나머지를 
#a 에 b를     

#mod를  b를    a를 b로 나눴을 때 나머지로 나눈   나머지? 
def func_a(a, b):
	mod = a % b
	while mod > 0:
		a = b
		b = mod
		mod = a % b
	return b

#1 부터 n까지  func를 만족하는 i, i? 수  아무튼 2번인거같은데 3개 수의 최대공약수 의 약수 의 개수 
def func_b(n):
	answer = 0
	for i in range(1, n+1):
		#최대 공약수의 약수라면? 
		if func_c(n, i):
			answer += 1
	return answer

#q 가 p의 약수인지? 
def func_c(p, q):
	if p % q == 0:
		return True
	else:
		return False

def solution(a, b, c):
    answer = 0
    #a c로 최대공약수 구하기 
    gcd = func_a(func_a(a, b), c)
    answer = func_b(gcd)
    return answer
