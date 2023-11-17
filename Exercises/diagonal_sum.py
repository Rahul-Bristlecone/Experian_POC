import math

arr = [11, 2, 4, 4, 5, 6, 10, 8, -12]
sum1 = 0
sum2 = 0
n = int(math.sqrt(len(arr)))
for i in range(0, len(arr), n + 1):
    sum1 += arr[i]
for j in range(n - 1, len(arr)-1, n - 1):
    print(arr[j])
    sum2 += arr[j]
print(sum1, sum2)
print(abs(sum1 - sum2))
