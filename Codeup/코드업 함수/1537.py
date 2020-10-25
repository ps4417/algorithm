# [기초-함수작성] 함수로 hello 또는 world 출력하기
def f(x):
    if x ==1 :
        print("hello")
    elif x ==2:
        print("world")
    else:
        print()

x = int(input())
f(x)