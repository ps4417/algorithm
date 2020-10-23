# 특별한 공던지기 2
# 공의 위치 n이 정수로 입력됨.(이번에는 정수로 입력됨)
# 공이 떨어지는 위치 n이 30≤n≤40 이거나 60≤n≤70 이면, win을 출력, 그외에는 lose를 출력한다.

n = int(input())
if 30<=n<=40 or 60<=n<=70:
    print("win")
else:
    print("lose")
