# [기초-배열연습] 2차원 배열 순서대로 채우기 1-5
# 다음과 같은 n*m 배열 구조를 출력해보자.

# 입력이 3 4인 경우 다음과 같이 출력한다.
# 12 11 10 9
# 8 7 6 5
# 4 3 2 1
# 입력이 n m인 경우의 2차원 배열을 출력해보자.

n,m = map(int,input().split())
for i in range(0,n):
    for j in range(0,m):
        print(m*(n-i)-j,end=' ')
    print()
