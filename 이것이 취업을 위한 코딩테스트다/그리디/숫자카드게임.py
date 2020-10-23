# n: 행, m: 열
# 뽑고자 하는 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
# 이것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑아야 한다.

# <min(), max() 내장 함수 사용해서 푸는방법>
 
n,m = map(int,input().split())

result = 0

# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int,input().split()))
    # 현재 줄에서 '가장 작은 수 찾기'
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result,min_value)
print(result)

