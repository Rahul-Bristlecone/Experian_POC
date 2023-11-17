arr = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
str1 = "zaba"
list1 = []
for i in str1:
    list1.append(arr[ord(i) - 97])

print(max(list1) * len(list1))

print(chr(ord('A')))
y = 4
z = lambda x: x * y
print(z(6))
