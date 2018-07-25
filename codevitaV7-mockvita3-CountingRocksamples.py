# Input
# 20 3
# 921 107 270 631 926 543 589 520 595 93 873 424 759 537 458 614 725 842 575 195
# 1 100
# 50 600
# 1 1000
# Output
# 1
# 12
# 20

import sys


def main():
    s, r = (map (int, sys.stdin.readline ().strip ().split (' ')))

    a = (list (map (int, sys.stdin.readline ().strip ().split (' '))))

    for i in range(0,r,+1):
        low,high = (map (int, sys.stdin.readline ().strip ().split (' ')))
        print(len(list(x for x in a if low <= x <= high)))



if __name__ == '__main__':
    main ()

