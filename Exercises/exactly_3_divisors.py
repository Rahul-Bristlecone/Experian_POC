def divisors(N):
    count = 0
    while count <= 3:
        for i in range(N):
            if i % i+1 == 0:
                return i
            count += 1
