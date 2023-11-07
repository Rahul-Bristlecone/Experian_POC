def findDigits(n):
    # Write your code here
    temp = n
    count = 0
    for i in range(len(str(n))):
        a = n % 10
        if a != 0:
            if temp % a == 0:
                count += 1
        n = n // 10
    return count


print(findDigits(114108089))
