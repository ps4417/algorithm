# 1부터 n까지 중 짝수의 합 구하기
n = int(input())
sum = 0
for i in range(1,n+1):
    if i % 2 ==0:
        sum = sum +i
print(sum)
