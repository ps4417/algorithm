# 아르바이트 가는 날
# 주원이는 월, 수, 금, 일 아르바이트를 간다.

# 다음은 요일의 순서이다.

# 1월요일
# 2화요일
# 3수요일
# 4목요일
# 5금요일
# 6토요일
# 7일요일
# 요일의 번호가 입력으로 주어지면 그 날이 아르바이트 가는 날이면 "oh my god"를 가는 날이 아니면 "enjoy"를 출력하시오.

ptj = int(input())
if ptj == 1 or ptj == 3 or ptj == 5 or ptj == 7:
    print("oh my god")
else:
    print("enjoy")