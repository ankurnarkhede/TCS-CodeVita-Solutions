n = int (input ("Enter the size of matrix:"))
r = n
c = n
t = 1
x = 0
y = 0
count=0
dict={}
a = [[0 for i in range (n)] for j in range (n)]

while (x <= r and y <= c):
    for i in range (y, c, +1):
        a[y][i] = t
        t += 1
    x += 1

    for i in range (x, r, +1):
        a[i][c - 1] = t
        t += 1
    c -= 1

    for i in range (c, y, -1):
        a[c][i - 1] = t
        t += 1
    r -= 1

    for i in range (r, x, -1):
        a[i - 1][y] = t
        t += 1
    y += 1

for i in range (0, n):
    for j in range (0, n):
        print ((a[i][j]),'\t', end='' )
    print ()


# for i in range (0, n):
#     for j in range (0, n):
#         if(a[i][j]%11==0):
#             count+=1
#
# print('Total Power points :',count+1)
#
# # print('(0,0)')
# for i in range (0, n):
#     for j in range (0, n):
#         if (a[i][j] % 11 == 0):
#             dict[a[i][j]]= (i,j)
#             # print('(',i,',',j,')', sep='')
#
# for i in sorted(list(dict.values())):
#     print(i, sep='')
#
# print(dict)
# print (sorted(list(dict.values())), sep='')