# 빠진 카드
# 우리는 1부터 N까지의 숫자가 차례대로 적힌 N장의 카드 묶음을 가지고 있다.

# 그런 데 이 카드 묶음을 옮기는 중 실수로 땅에 떨어뜨려 그 중 한 장을 잃어버렸다.

# 여러 분은 땅에 떨어진 카드 묶음을 읽어서 빠진 하나의 카드 번호를 찾아 출력해야 한다.

# 첫 줄에는 한 장을 잃어버리기 전 카드의 전체 장수 N이 주어져 있다. 단 . 3 <= N <= 50 이다.

# 이어지는 N-1개의 각 줄에는 한 장이 빠진 카드 묶음의 카드 숫자가 하나씩 순서 없이 나열되어 있다.

n = int(input())
cards = []
miss = []

for i in range(1,n+1): # 1~n까지의 숫자카드
    cards.append(i)

for i in range(0,n-1): # n-1개의 카드(0번쨰~n-2번쨰)
    num = int(input())
    miss.append(num)

for card in miss:
    cards.remove(card)
print(cards[0])

