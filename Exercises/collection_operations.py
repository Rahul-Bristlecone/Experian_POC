if __name__ == "__main__":
    a = int(input())  # total no. of shoes
    size_list = list(map(int, input().split()))
    customer = int(input())
    temp = []
    while customer > 0:
        shoe = list(input().split())
        if shoe[0] in size_list:
            temp.append(int(shoe[1]))
            print(temp)
        customer -= 1

    print(sum(temp))
