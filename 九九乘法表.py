for x in range(1, 10):
    for y in range(1, x + 1):
        print("%d x %d = %d" % (y, x, x * y), end="\t")
    print()
