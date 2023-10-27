if __name__ == '__main__':
    list1 = []
    marks = []
    for _ in range(int(input())):
        list2 = []
        name = input()
        score = float(input())
        list2.append(name)
        list2.append(score)
        print(list2)
        list1.append(list2)

        # a = (sorted(marks.append(score)))[1]
    print(sorted(list1))

    # for name, score in list1:
    #     if score == a:
    #         print(name)