import math


def digitsInFactorial(N):
    if N < 0:
        return 0
    if N <= 1:
        return 1
    else:
        digits = 0
        for i in range(2, N + 1):
            digits += math.log10(i)
        return math.floor(digits) + 1

print(digitsInFactorial(8))
