# 공포도 X 인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 한다.
# 모험가 수 > 공포도


n = int(input())  # 모험가 수
data = list(map(int,input().split()))  # 공포도
data.sort()  # 공포도 오름차순 

result = 0  # 총 그룹 수
count = 0  # 현재 그룹에 포함된 모험가의 수

for i in data:      # 공포도를 낮은 것부터 하나씩 확인하며
    count+=1        # 현재 그룹에 모험가를 포함시키기
    if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result+=1   # 총 그룹의 수 증가시키기
        count = 0   # 현재 그룹에 포함된 모험가의 수 초기화

print(result)


