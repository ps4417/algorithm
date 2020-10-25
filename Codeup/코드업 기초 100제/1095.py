# [기초-1차원배열] 이상한 출석 번호 부르기3
n = int(input())
k = list(map(int,input().split()))
max = 217000000
for i in k:
    if i<max:
        max=i
    if i == max:
        max = i
print(max)
