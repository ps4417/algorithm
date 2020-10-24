# First Special Judge (Test)

# 10개의 수가 입력된다.

# 10개의 수 중 5의 배수를 하나만 출력한다.

# 만약 5의 배수가 없다면 0을 출력한다.

data = map(int,input().split())
data = list(data)
x = False
# print(data)
for i in data:
    if i % 5 ==0:
        x = True
        print(i)
        break
if not x:
    print('0')   
        