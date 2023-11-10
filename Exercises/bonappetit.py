bill = [3, 10, 2, 9]
k = 1
b = 7
if (sum(bill) - bill[k])/2 == b:
    print("BonAppetit")
else:
    print((b - (sum(bill) - bill[k])//2))
