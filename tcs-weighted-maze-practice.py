import sys


def main():
    n = int (sys.stdin.readline ().strip ())
    ip = [[0 for i in range (n)] for j in range (n)]

    for i in range (0, n, +1):
        a = (list (map (int, sys.stdin.readline ().strip ().split (','))))
        for j in range (0, len (a), +1):
            ip[i][j] = a[j]

    # print('Entered maze=',ip)

    x = y = 0
    current = ip[0][0]
    prev = current
    iteration = 0

    while (x != n - 1 or y != n - 1):
        iteration += 1

        try:
            adj_min = min (ip[x][y + 1], ip[x + 1][y])

            if (adj_min == ip[x][y + 1]):
                y += 1
            else:
                x += 1

        except(IndexError):
            if (x == n - 1):
                adj_min = ip[x][y + 1]
                y += 1
            elif (y == n - 1):
                adj_min = ip[x + 1][y]
                x += 1

                # print('adj_min=',adj_min)

        prev = int (current)
        current = adj_min


        # print ('Iteration={}, current={}, prev={}'.format (iteration,current, prev))
        # print('x={}, y={}'.format(x,y))

    # print('FINAL=======current={}, prev={}'.format(current,prev))

    print (prev)


if __name__ == '__main__':
    main ()
