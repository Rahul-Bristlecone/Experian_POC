from itertools import permutations

s = list(input().split())
# size = int(input())

for i in sorted(list(permutations(s[0], int(s[1])))):
    print(''.join(i))
