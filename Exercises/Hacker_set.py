def check_subset(set1, set2):
    return set(set1).issubset(set(set2))


if __name__ == "__main__":
    n = int(input())
    while n > 0:
        a = int(input())
        setA = list(map(int, input().split()))
        b = int(input())
        setB = list(map(int, input().split()))
        result = check_subset(setA, setB)
        print(result)
        n -= 1
