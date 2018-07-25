
import sys
import string


def sum_digits(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r


def int2base(integer, base):
    if not integer: return '0'
    sign = 1 if integer > 0 else -1
    alphanum = string.digits + string.ascii_lowercase
    nums = alphanum[:base]
    res = ''
    integer *= sign
    while integer:
        integer, mod = divmod (integer, base)
        res += nums[mod]
    return ('' if sign == 1 else '-') + res[::-1]


def main():
    a_base_6 = []
    derived_sequence=[]
    inversions_count=0

    n = int (sys.stdin.readline ())

    a = (list (map (int , sys.stdin.readline ().strip ().split (','))))

    for i in range (0, n, +1):
        a_base_6.append (int(int2base(a[i], 6)))
        derived_sequence.append(sum_digits(a_base_6[i]))

    for i in range(0,n,+1):
        for j in range(i+1,n,+1):
            if(derived_sequence[i]>derived_sequence[j]):
                inversions_count+=1

    print(inversions_count)


if __name__ == '__main__':
    main ()
