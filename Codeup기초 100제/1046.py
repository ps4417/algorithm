#  정수 3개 입력받아 합과 평균 출력하기(평균은 둘째자리에서 반올림)
a,b,c = map(int,input().split())
print(a+b+c)
av = (a+b+c)/3
print("%.1f" %av)