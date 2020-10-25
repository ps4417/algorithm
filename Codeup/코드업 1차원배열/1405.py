# 숫자 로테이션
# n개의 숫자가 입력되면,

# n개의 숫자를 왼쪽으로 하나씩 돌려서 출력하시오.

# 예) 1 2 3 4 5가 입력된 경우,

# 1 2 3 4 5
# 2 3 4 5 1
# 3 4 5 1 2
# 4 5 1 2 3
# 5 1 2 3 4

n = int(input())
data = list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        print(data[j],end=' ')
    print()
    for k in range(n-1):
        temp = data[k]
        data[k] = data[k+1]
        data[k+1]=temp