/*
반복문을 사용하여 내부는 ‘+’, 가장자리는 ‘*’인 아래와 같은 다이아몬드를 만드세요. ( 매 행 두 번째 * 이후로는 공백이 아니고 개행을 바로 해주시기 바랍니다. )
*/

n = 5
for i in range(n):
	# space
	for j in range(n-i):
		print(' ',end='') #공백을 한 줄에 프린트 함.
	print('*',end='')
	for j in range(2*i):
		print('+',end='')
	print('*')
# k 루프는 가운데 줄이랑 그 이후 다이아 아래쪽 반
for k in range(n+1):
	# space
	for j in range(k): 
		print(' ',end='')
	print('*',end='')
	for j in range(2*(n-k)):
		print('+',end='')
	print('*')


# 삼각형 문제
     *
    **
   *+*
  *++*
 *+++*
******

n = 5

for i in range(n+1):
    print((n-i)*' ', end='')
    if i ==0:
        print("*")
        continue
    print("*", end='')

    print(bool(i<n)*(i-1)*"+" + bool(i>=n)*(i-1)*"*", end='')

    if i < n: #마지막 줄도 첫번째 줄도 아닐 때
        print((i-1)*"+", end='')
    else:
        print((i-1)*"*", end='')
    
    print("*") #0번째 줄을 제외한 다른 줄들의 오른쪽 끝
