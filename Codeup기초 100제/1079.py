# [기초-종합]원하는 문자가 입력될 때까지 반복 출력하기
List = input().split()
for i in List:
    if i=="q":
        print(i)
        break
    else:
        print(i)
