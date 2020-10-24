# 두 수 사이의 홀수 출력하기
a,b = map(int,input().split())
for i in range(a,b+1):
    if i%2==1:
        print(i,end=' ')