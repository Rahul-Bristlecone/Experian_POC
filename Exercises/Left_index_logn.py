def leftIndex(N, arr, X):
    # code here
    for i in arr:
        if X == i:
            return arr.index(X)


N = 6
arr1 = [1, 1, 2, 2, 3, 6]
X = 2

print(leftIndex(N, arr1, X))
