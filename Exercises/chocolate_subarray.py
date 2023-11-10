arr = [1,2,2,1,5,6]
m = 1
d = 6
count = 0
for i in range(len(arr)):
    if sum(arr[i:i+m]) == d:
        count = count+1
print(count)