# [기초-종합] 16진수 구구단
a = input()
b = int(a,16)
for i in range(1,16):
    print("%s*%X=%X" %(a,i,b*i))
    