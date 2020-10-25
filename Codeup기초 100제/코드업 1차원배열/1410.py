# 올바른 괄호 1 (괄호 개수 세기)
data = input()
count1 = 0
count2 = 0
for x in data:
    if x == "(":
        count1 +=1
    elif x == ")":
        count2 +=1
print(count1,count2,end=" ")
