# [기초-조건/선택실행구조] 정수 1개 입력받아 분석하기
a = int(input())
if a>0:
    if a%2==0:
        print("plus")
        print("even")
    else:
        print("plus")
        print("odd")
else:
    if a%2==0:
        print("minus")
        print("even")
    else:
        print("minus")
        print("odd")


    