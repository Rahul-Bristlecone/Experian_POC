size = 5
for n in range(1,int(size)+1):
    print("0"*(size-1)+"*"*n, end="")  # restrict creating new line
    print("\r")
    size = size-1
