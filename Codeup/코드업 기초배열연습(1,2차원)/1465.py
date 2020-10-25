# [기초-배열연습] 2차원 배열 순서대로 채우기 1-6
# 다음과 같은 n*m 배열 구조를 출력해보자.

# 입력이 3 4인 경우 다음과 같이 출력한다.
# 9 10 11 12
# 5 6 7 8
# 1 2 3 4

# 입력이 n m인 경우의 2차원 배열을 출력해보자.

# 내 풀이

# n,m = map(int,input().split())
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         print(n*(m-1)+(j-1)-m*(i-1),end=' ')
#     print()

n,m = map(int,input().split())

for i in range(n-1,-1,-1):
    for j in range(1,m+1):
        print(i*m+j, end=' ')
    print()
