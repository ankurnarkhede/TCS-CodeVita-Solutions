
total=int(input())
days=0
p=[]
w=[]
for i in range(0,total,+1):
    p.append(0)
    w.append(0)


for i in range(0,total,+1):
    p[i], w[i] = (map (int, input ().strip ().split (' ')))

for i in range (0, total, +1):
    # print('papermints=',p[i],'wrapper=',w[i])

# days=int(p+((p+w)/7))
    days=p[i]
    # print('Initial days=============',days)

    while((p[i]+w[i])>6):
        # print('Now p and w=',p[i],w)
        w[i]+=p[i]
        # print("w=",w[i])

        p[i]=w[i]//7
        # print ("p=", p[i])

        w[i]=w[i]%7
        # print ("w=", w[i])

        days+=p[i]

        # print('now days=================',days)


    # print('days=', days)
    print(days)

