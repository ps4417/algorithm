# [기초-삼항연산] 두 정수 입력받아 큰 수 출력하기
a,b = map(int,input().split())
print(a if a>b else b)