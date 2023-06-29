/*
시작 값과 끝 값을 입력받아
시작 값 이상 끝 값 미만에 있는 모든 짝수를 차례로 출력하는 코드를 작성하세요.
한 space 씩 뛰어서 출력하기 위해 print(…, end=’ ‘)를 활용하세요.

시작 값과 끝 값을 차례로 입력받습니다.
시작 값 이상 끝 값 미만에 있는 모든 짝수를 출력하세요.
*/

start_value = int(input())
end_value = int(input())

#출력 부분
for i in range(start_value, end_value):
    if i%2==0:
        print(i, end=' ') # 한 space 씩 뛰어서 출력하는 출력문
