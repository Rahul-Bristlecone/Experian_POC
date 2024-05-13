# def getByIndex(arr,n,idx):
#     # return required ans
#     for i in range(0,n):
#         if i == idx:
#             return arr[i]
#     else:
#         return -1

def deleteFromArray(arr, n, idx):
    # code here
    for i in range(idx, n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = 0
    return arr

n = 5
arr = [1, 2, 3, 4, 5]
idx = 8
print(deleteFromArray(arr, n, idx))
