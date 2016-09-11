def swapneg(a):
    for e in a:
        if e < 0:
            index = a.index(e)
            a[index] = "Dojo"
    print a
swapneg([1,2,-3,-4,5])