def inversionCount(arr, n):
    # Your Code Here
    count = 0
    for i in range(n):
        x = arr[i]
        for j in range(i+1,n):
            if arr[j] < x:
                count += 1
    return count


arr1 = [2, 4, 1, 3, 5]
n = 5
print(inversionCount(arr1, n))
