# [기초-종합] 소리 파일 저장용량 계산하기
h,b,c,s = map(int,input().split())
byte = (h*b*c*s)/8
kb = byte/1024
mb = round(kb/1024,1)
print("{0} MB".format(mb))
