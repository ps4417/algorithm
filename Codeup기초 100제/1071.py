# [기초-반복실행구조] 0 입력될 때까지 무한 출력하기1
a = input().split()

for i in a:
    if int(i)==0:
        break
    else:
        print(int(i))