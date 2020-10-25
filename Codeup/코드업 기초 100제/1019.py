# 연월일 입력받아 그대로 출력하기
a,b,c=input().split(".")
print("%.04d" %int(a),end=".")
print("%.02d" %int(b),end=".")
print("%.02d" %int(c))