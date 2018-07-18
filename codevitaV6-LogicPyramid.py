
n=int(input())
# n=5

s=[]
ser=[]
k=0

for i in range(3,500,1):
    s.append(int((i*(i+1))/2))


for j in range(0,497,4):
    ser.append(s[j])


for i in range(0,n,1):
    for j in range(0,i+1,1):
        print((str(ser[k])).zfill(5), end=' ')
        k+=1
    if(i==n-1):
        break
    print()