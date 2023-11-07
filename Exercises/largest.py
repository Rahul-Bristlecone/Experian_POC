# a = int(input())
# b = int(input())
# c = int(input())
#
# if (a > b) and (a > c):
#     print(a)
# elif (b > a) and (b > c):
#     print(b)
# elif (c > a) and (c > b):
#     print(c)

# for num in range(10, 14):
#     for i in range(2, num):
#         if num % i == 1:
#             print(num)
#             break

x1 = 0
v1 = 2
x2 = 5
v2 = 3
if v1 > v2 and x1 < x2:
    if (x1 - x2 != 0) and (v1 - v2 != 0) and (x1 - x2) % (v1 - v2) == 0:
        print("YES")
    else:
        print("NO")

else:
    print("NO")
