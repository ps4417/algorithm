#  [기초-배열연습] 2차원 배열 순서대로 채우기 1-1

# 다음과 같은 n*n 배열 구조를 출력해보자.

# 입력이 3인 경우 다음과 같이 출력한다.
# 1 2 3
# 4 5 6
# 7 8 9

# 입력이 n인 경우의 2차원 배열을 출력해보자.

# a = 0
# n = int(input())
# for i in range(n):
#     for j in range(n):
#         a += 1
#         print(a,end=' ')
#     print()

n = int(input())
for i in range(n):
    for j in range(1,n+1):
        print(n*i+j,end=' ')
    print()