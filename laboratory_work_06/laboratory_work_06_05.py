from random import randint

def create_m(rows, cols):
    numbers = list(range(1, 53))
    for i in range(len(numbers) - 1, 0, -1):
        j = randint(0, i)
        numbers[i], numbers[j] = numbers[j], numbers[i]
    matrix = []
    k = 0
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(numbers[k])
            k += 1
        matrix.append(row)
    return matrix

with open("lab6_5_in.txt", "r") as fi, \
        open("lab6_5_ou.txt", "w") as fo:
    next(fi)
    line = fi.readline()
    (rows, cols) = line.split()
    rows = int(rows)
    cols = int(cols)

    fo.write("вариант 27\n")

    my_matrix = create_m(rows, cols)

    for row in my_matrix:
        for x in row:
            fo.write("{0:>5}".format(x))
        fo.write("\n")