def insertAtIndex(self, arr, sizeOfArray, index, element):
    # Your code here
    return arr[:index] + [element] + arr[index:]

element = 3
arr = {1,2,3,4,5,6}
index = 3
sizeOfArray = 6

print(insertAtIndex(arr, sizeOfArray, index, element))
