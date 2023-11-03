happ = 0
list1 = list((input().split()))
a = set(input().split())
b = set(input().split())

for i in list1:
    if i in a:
        happ += 1
    elif i in b:
        happ -= 1

print(happ)