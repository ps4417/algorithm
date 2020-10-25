# 수 나열하기(등차수열)
# 시작 값(a), 등차의 값(d), 몇 번째 수 인지를 의미하는 정수(n)가
# 공백을 두고 입력된다.(모두 0 ~ 100)
# n번째 수를 출력한다.
# a1 + (n-1)d
a,d,n = input().split()
result = int(a) + (int(n)-1)*int(d)
print(result)


