# 기억력 테스트 1
#첫째 줄에 숫자 10개가 차례대로 입력된다.

# 둘째 줄에 k값이 입력된다. 
# k번째 숫자가 무엇이었는지 출력한다.

data = list(map(int,input().split()))
n = int(input())
print(data[n-1])
