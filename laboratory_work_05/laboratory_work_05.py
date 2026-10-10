from random import randint
print("вариант 27")
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

my_matrix = create_m(4, 13)
print(my_matrix)
