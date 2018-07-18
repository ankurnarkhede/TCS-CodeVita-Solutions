

import itertools

total=int(input("input total:"))
r=[]
z=[]
n=0
sum=0

l1 = [0,1,2,3,4,5,6,7,8,9]
len0=len(l1)
# print("length of set=",len0)

a=list(itertools.permutations(l1))
# print("a=", a)

# a_sorted=sorted(a)
a_sorted=a
# print("a_sorted=", a_sorted)

for i in range(0,total,+1):
    n = 0
    r.append(int(input()))

    for j in range(0,len0,+1):
        n=n+10**(len0-1-j)*a_sorted[r[i]-1][j]
    # print("rank of",r[i],'is=',n)
    sum+=n


# print("sum =",sum)
print(sum)



