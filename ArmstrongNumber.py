armstrong=[]
for i in range(501):
    num=i
    result=0
    n=len(str(i))
    for j in range(1,n+1):
        result+=(num%10)**n
        num//=10
    if(i==result):
        armstrong.append(str(i))
print(", ".join(armstrong))
