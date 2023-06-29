/* 
민수는 마트에서 사과 x개와 바나나 y개를 사려고 한다. 사과와 바나나의 가격이 각각 1.35달러, 2.67달러 일 때 총 계산해야 할 금액을 소수 둘째 자리에서 반올림하여 소수 첫자리까지 표현하는 코드를 작성하세요.
*/
apple = 1.35
banana = 2.67
x = int(input())
y = int(input())
print(f'{x*apple+y*banana:.1f}') # 출력부분

# 올림, 버림 함수
# ceil, floor --> import math
cost = math.ceil(x *apple + y* banana)
print(cost)

# 올림 함수
n = 2.3
int(n) + bool(n%1) #도 가능
