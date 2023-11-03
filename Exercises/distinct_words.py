import collections
a = int(input())
s =[]
for i in range(a):
    b = input()
    s.append(b)

print(len(set(s)))
count = collections.Counter(s)
new_dict = dict(count)
for i in new_dict:
    print (new_dict[i])


