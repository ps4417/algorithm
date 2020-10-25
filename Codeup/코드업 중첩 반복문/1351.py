# 구구단 출력하기 2
# 시작 단과 마지막 단을 입력한다.(정수1~9)
# 예시처럼 구구단을 출력한다.

a,b = map(int,input().split())
for i in range(a,b+1):
    for j in range(1,10):
        print("{0}*{1}={2}".format(i,j,i*j))