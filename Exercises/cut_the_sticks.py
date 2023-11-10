def cutThesticks(arr):
    sticks = []
    new_arr = set(arr)
    new_list = list(new_arr)
    new_list.sort()
    for i in new_list:
        count = 0
        for j in range(len(arr)):
            if i <= arr[j]:
                count += 1
        sticks.append(count)
    return sticks


arr = [1, 2, 3, 4, 3, 3, 2, 1]
result = cutThesticks(arr)
print(result)
