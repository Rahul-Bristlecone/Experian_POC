def sort_merge(arr1, arr2):
    sort_array = []
    i, j = 0, 0
    x, y = len(arr1), len(arr2)

    while i < x and j < y:
        if arr1[i] >= arr2[j]:
            sort_array.append(arr2[j])
            j = j + 1
        else:
            sort_array.append(arr1[i])
            i = i + 1

    while i < x:
        sort_array.append(arr1[i])
        i = i + 1

    while j < y:
        sort_array.append(arr2[j])
        j = j + 1

    return sort_array


arr1 = [8, 11]
arr2 = [3, 5, 9, 23]
print(sort_merge(arr1, arr2))
