# 세 수 정렬하기
#세 수를 오름차순으로 정렬하려고 한다. (낮은 숫자 -> 높은 숫자)

# 예)

# 5 8 2   ====> 2 5 8    로 출력

data = list(map(int,input().split()))
data.sort()
for i in data:
    print(i,end=' ')