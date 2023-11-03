a = [2, 3, 1, 4, 0, 5, 6, 7]
for i in a:
    if i == 0:
        a.remove(i)
        a.append(i)
print(a)
