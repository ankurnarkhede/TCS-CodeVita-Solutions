# Input
#
# 5
#
# 55, 53, 88, 27, 33
#
# Output
#
# 8

import sys

derived_sequence=[]


def count_binary(number):
    derived_binary= bin(number)[2:].replace('0','')
    return derived_binary.count('1')



def main():

    inversions_count = 0
    n = int (sys.stdin.readline ().strip())

    a = list (map (int, sys.stdin.readline ().strip ().split (',')))

    for i in range(0,n,+1):
        derived_sequence.append(int(count_binary(a[i])))

    # print('Derived seq=',derived_sequence)

    for i in range(0,n,+1):
        for j in range(i+1,n,+1):
            if(derived_sequence[i]>derived_sequence[j]):
                inversions_count+=1

    # print('Incersions_count=',inversions_count)
    print(inversions_count)


if __name__ == "__main__":
    main ()



