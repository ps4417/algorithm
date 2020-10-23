# 주어진 수들을 M번 더해 가장 큰수를 만들어라. 단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다. 
# 배열의 크기 N, 숫자가 더해지는 횟수 M,최대 더해질 수 있는 횟수 K

# 입력 예시
# 5 8 3
# 2 4 5 4 6

# 출력예시
# 46

 
# 입력 받기
n,m,k = map(int,input().split())

# n개의 자연수를 list에 담아 data 변수에 넣기
data = list(map(int,input().split()))

data.sort() # 오름차순 정렬  ex) 2 4 4 5 6

first = data[n-1] # 가장 큰 수 ex) 6
second = data[n-2] # 두번째로 큰 수 ex) 5

result = 0

while True:
    for i in range(k): # 가장 큰 수 k번 더하기
        if m == 0: # m이 0 이면 반복문 탈출
            break
        result += first
        m -= 1  # 더할 때마다 1씩 빼기
    if m == 0:
        break
    result += second  # 두 번째로 큰 수를 더하기
    m -= 1  # 더할 때마다 1씩 빼기 
    # 다시 맨 위에 for문 시작

print(result)


