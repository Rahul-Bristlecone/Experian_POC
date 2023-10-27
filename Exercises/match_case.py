if __name__ == '__main__':
    N = int(input())
    list1 = []
    operations = input("Enter operation")

    match operations:
        case '1':
            a = int(input("Enter the position i"))
            b = input("input the number")
            list1.insert(a, b)
        case '2': print(list1)
        case '3':
            pass
        case '4':
            pass
        case '5':
            pass
        case '6':
            pass
        case '7':
            pass
        case other:
            pass
