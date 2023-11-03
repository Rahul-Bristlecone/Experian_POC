a = [1, 3, 2, 5, 4, 6, 9, 0]
target = int(input())
list1 = []
for i in range(len(a)):
    temp = target - a[i]
    if temp in list1:
        print (temp, a[i])
    list1.append(a[i])