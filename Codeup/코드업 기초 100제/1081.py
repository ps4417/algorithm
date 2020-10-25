# [기초-종합] 주사위를 2개 던지면?
a,b = map(int,input().split())
for i in range(1,a+1):
    for j in range(1,b+1):
        print(i,j)