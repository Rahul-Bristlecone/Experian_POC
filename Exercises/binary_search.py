def searchInSorted(arr, N, K):
    # Your code here
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == K:
            return mid
        elif arr[mid] < K:
            low = mid + 1
        else:
            high = mid - 1
    return -1


arr1 = [1, 2, 3, 4, 5, 6]
N = 5
K = 6
print(searchInSorted(arr1, N, K))
