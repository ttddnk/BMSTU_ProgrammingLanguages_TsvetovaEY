from math import *
print("вариант 27")
xb = float(input('Введите Xbeg='))
xe = float(input('Введите Xend='))
dx = float(input('Введите Dx='))
print("Xbeg={0: 7.2f} Xend={1: 7.2f}".format(xb, xe))
print(" Dx={0: 7.2f}".format(dx))
xt = xb
print("+--------+--------+")
print("I    X   I    Y   I")
print("+--------+--------+")

while xt <= xe:
    if xt <= -2.5:
        y = -6/7*xt - 36/7
    elif -2.5 <= xt <= 2:
        y = (xt + 2)*(xt + 1)*(xt - 1.5)
    elif xt >= 2:
        y = -2*xt + 10

    print("I{0: 7.2f} I{1: 7.2f} I".format(xt, y))
    xt += dx
print("+--------+--------+")

