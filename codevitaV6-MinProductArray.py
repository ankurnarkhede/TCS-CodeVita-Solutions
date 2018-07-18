
a=[]
b=[]
lar_b=0
sum=0
lar_b_index=0

n, k = (map(int, input ().strip ().split (' ')))
a = (list (map (int, input ().strip ().split (' '))))
b = (list (map (int, input ().strip ().split (' '))))

print('n=',n,'k=',k,'a=',a,'b=',b)

for i in range(0, len(b),1):
    if(abs(b[i])>lar_b):
        lar_b=abs(b[i])
        lar_b_index=i

if(b[lar_b_index]>0):
    temp_a=a[lar_b_index]
    a[lar_b_index]=a[lar_b_index]+(-2*k)
else:
    temp_a=a[lar_b_index]
    a[lar_b_index]=a[lar_b_index]+(2*k)

for i in range(0,n,1):
    sum+=(a[i]*b[i])

print('Min_product_array=',sum)


