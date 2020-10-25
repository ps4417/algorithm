# [기초-함수작성] 함수로 가장 작은 값 리턴하기



def f():
    min = data[0]
    for i in range(n):
        if data[i]<min:
            min = data[i]
    return min

n = int(input())
data = list(map(int,input().split()))
print(f())


