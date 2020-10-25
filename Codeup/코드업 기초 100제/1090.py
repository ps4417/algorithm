# 수 나열하기(등비수열)
# result = a1* r^n
# a1=2, r=3, n=

a,r,n = input().split()
result= int(a) *pow(int(r),int(n)-1)
print(result)
