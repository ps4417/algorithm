# [기초-종합] 언제까지 더해야 할까?
n = int(input())
sum = 0
for i in range(1,n+1):
    sum=sum+i
    if sum>=n:
        print(i)
        break   