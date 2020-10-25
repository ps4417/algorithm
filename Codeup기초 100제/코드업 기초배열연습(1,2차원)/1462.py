# [기초-배열연습] 2차원 배열 순서대로 채우기 1-3
# 다음과 같은 n*n 배열 구조를 출력해보자.

# 입력이 3인 경우 다음과 같이 출력한다.
# 1 4 7
# 2 5 8
# 3 6 9
# 입력이 n인 경우의 2차원 배열을 출력해보자.

n = int(input())

for i in range(1,n+1):
    for j in range(0,n):
        print(i+j*n,end=' ')
    print()