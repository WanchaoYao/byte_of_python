array = [[] for i in range(9)]
for i in range(1,10):
    array[i - 1] = ["%d * %d = %d"%(j, i, j * i) for j in range(1, i + 1)]
    print array[i - 1]
