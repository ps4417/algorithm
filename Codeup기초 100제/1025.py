# 정수 1개 입력받아 나누어 출력하기
a = input()
count = len(a)-1
for i in range(len(a)):
    # print("["+(a[i]+'0'*count)+"]")
    print([int(a[i]+'0'*count)])
    count-=1