# [기초-2차원배열] 바둑판에 흰 돌 놓기
arra = [[0]*19 for i in range(19)]
n = int(input())
for i in range(n):    
    x,y = map(int,input().split())
    arra[x-1][y-1] = 1

for i in range(19):
    for j in range(19):
        print(arra[i][j], end=' ')
    print()

    

