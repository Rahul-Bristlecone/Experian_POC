def print_rangoli(size):
    for n in range(size):
        for m in range(size, 0):
            print("* ", end="")  # restrict creating new line
        print("\r")


if __name__ == '__main__':
    n = int(input("Enter rangoli size"))
    print_rangoli(n)
