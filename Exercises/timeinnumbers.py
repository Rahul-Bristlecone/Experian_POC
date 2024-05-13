def timeInWords(h, m):
    # Write your code here\
    if m == 0:
        print(h + "'o' clock'")
    elif 1 <= m <= 30:
        print(m + "past" + h)
    else:
        print(str(60 - int(m)) + "to" + str(h+1))

h = 4
m = 43
timeInWords(h,m)