# 큰수 - 작은수
a,b = map(int,input().split())
if a>b:
    result = a-b
    print(result)
else:
    result = b-a
    print(result)