def saveThePrisoner(n, m, s):
    # Write your code here
    remainder = (m + s - 1) % n
    if (m + s - 1) % n == 0:
        return n
    else:
        return remainder


saveThePrisoner(7, 19, 2)
# n - prisoners
# m - candies
# s - start position
# trick - make the start postion 0
