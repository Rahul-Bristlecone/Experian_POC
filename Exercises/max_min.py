def miniMaxSum(arr):
    # Write your code here
    return sum(arr) - max(arr), sum(arr) - min(arr)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
