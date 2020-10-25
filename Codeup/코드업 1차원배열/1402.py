# 거꾸로 출력하기 3
n = int(input())
data = list(map(int,input().split()))
data.reverse()
for i in data:
    print(i,end=" ")  
