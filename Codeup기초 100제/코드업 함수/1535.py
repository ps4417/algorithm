# [기초-함수작성] 함수로 가장 큰 값 위치 리턴하기
# 첫 줄에 데이터의 개수 n이 입력된다.

# 두 번째 줄에 n개의 데이터가 공백을 두고 입력된다.
# 가장 큰 값이 처음 나타나는 위치를 출력한다.

def f():
    min = data[0]
    cnt = 0
    for i in range(n):
        if data[i]>min:
            min=data[i]
            cnt = i
    return cnt+1

n = int(input())
data = list(map(int,input().split()))
print(f())

