# def theSequence(n):
#     # code here
#     if n == 0:
#         return 1
#     return n + (n * (theSequence(n - 1)))
#
#
# print(theSequence(3))

def sumOfDigits( n):
    '''
    :param n: given number
    :return: sum of digits of n.
    '''
    # code here
    s = 0
    while n != 0:
        s = s + n % 10
        n = n // 10

    return s


print(sumOfDigits(45))
