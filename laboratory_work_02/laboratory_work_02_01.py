from math import sin, pi
print("вариант 27")
x = float(input("введите значение х = "))

if x <= -2.5:
    y = -6/7*x - 36/7
elif -2.5 <= x <= 2:
    y = (x + 2)*(x + 1)*(x - 1.5)
elif x >= 2:
    y = -2*x + 10

print("X = {0:.2f} Y = {1:.2f}".format(x, y))





