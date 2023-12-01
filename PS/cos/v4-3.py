# 처음에 dp 비슷하다고 생각 했다.  이용권이  비용과 사용일수(이득)  2개의 속성을 갖기 때문이다.
# dp의 경우 여러개의 이용권이 있다고 했을 때 n이 딱 나누어 떨어지지 않아서  
#일수 당 비용이 적은 것을 많이 골라서 하면 떨어지지 않아 더 많이 
#비용을 쓸 수 있다. 
# 이 문제는 1원과 5원, 2개가 있고 1원이 있어서 나누어 떨어진다.
def solution(one_day_price, multi_day, multi_day_price, n):
    if one_day_price * multi_day <= multi_day_price:
        return n * one_day_price
    else:
        return (n // multi_day) * multi_day_price + (n % multi_day) * one_day_price
        
