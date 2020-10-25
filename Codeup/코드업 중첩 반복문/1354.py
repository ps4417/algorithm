# 삼각형 출력하기 2
# 길이 n이 입력되면 역삼각형을 출력한다.

# 예)

# n이 5이면

# *****
# ****
# ***
# **
# *

n = int(input())
for i in range(1,n+1):
    for j in range(0,n-i+1):
        print("*",end='')
    print('')
