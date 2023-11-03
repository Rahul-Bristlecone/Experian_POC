def average(array):
    # your code goes here
    set1 = set(array)
    set_sum = sum(set1)
    return set_sum/len(set1)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
