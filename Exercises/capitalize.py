def solve(s):
    list1 = s.split()
    for word in list1:
        " ".join(word.capitalize())


if __name__ == '__main__':
    s = input()
    print(solve(s))
