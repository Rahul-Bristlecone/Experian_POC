# def findFloor(A, N, X):
#     # Your code here
#     for i in A:
#         if i > X:
#             break
#         elif A[N-1] == i:
#             return N-1
#     return A.index(i) - 1
#
#
# arr1 = [1, 2, 8, 10, 11, 12, 19]
# X = 21
# N = 7
# print(findFloor(arr1,N, X))

def peakElement(arr, n):
    # Code here
    for i in range(1, n):
        if arr[0] == max(arr) and n > 1:
            return 0
        elif arr[n - 1] == max(arr) and n > 1:
            return n - 1
        elif arr[i + 1] < arr[i] > arr[i - 1]:
            return 1
        else:
            return 1


arr = [15]
N = 1
print(peakElement(arr, N))
