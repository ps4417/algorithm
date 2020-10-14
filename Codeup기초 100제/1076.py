# [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기
a= input()
n = ord(a)
i = ord("a")

while i<=n:
    print(chr(i),end=" ")
    i+=1

