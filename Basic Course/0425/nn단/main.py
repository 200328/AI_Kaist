/*
아래와 같이 nn단을 출력하는 반복문 코드를 작성하세요.
nn단이란 구구단에서 1 x 1에서 n x n까지만 나타낸 것.
구구단의 두 피연산자가 1이상 n이하이다.
각 단이 끝난 후에는 한 줄 띄기 (해당 위치에 print()를 추가하면 된다.)가 있어야 한다.
*/

n = int(input())

for i in range(1,n+1):
    for j in range(1,n+1):
        print(f'{i} x {j} = {i*j}')
    print()
