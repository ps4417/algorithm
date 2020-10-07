# 정수 2개 입력받아 자동 계산하기
# 첫 줄에 합
# 둘째 줄에 차,
# 셋째 줄에 곱,
# 넷째 줄에 몫,
# 다섯째 줄에 나머지,
# 여섯째 줄에 나눈 값을 순서대로 출력한다.
# (실수, 소수점 이하 셋째 자리에서 반올림해 둘째 자리까지 출력)
a,b = input().split()
print(int(a)+int(b))
print(int(a)-int(b))
print(int(a)*int(b))
print(int(int(a)/int(b)))
print(int(a)%int(b))
print("%.2f" %(int(a)/int(b)))