from math import *
from random import *

with open("lab6_4_in.txt", "r") as fi, \
        open("lab6_4_ou.txt", "w") as fo:
    next(fi)
    line = fi.readline()
    (n, y) = line.split()
    n = int(n)
    y = float(y)

    if n > 30:
        n = 30
    elif n < 5:
        n = 5

    fo.write("Начальное состояние\n")
    mas = []
    for i in range(n):
        mas.append(uniform(-5, 5))
        fo.write("{0: 7.3f}".format(mas[i]))
    fo.write("\n")

    amin = mas[0]
    amax = mas[0]
    for i in range(1, n):
        if mas[i] < amin:
            amin = mas[i]
        if mas[i] > amax:
            amax = mas[i]

    fo.write("amin={0:7.3f} amax={1:7.3f}\n".format(amin, amax))

    if not (amin < y < amax):
        y = (amin + amax) / 2

    asum = 0.0
    aprd = 1.0
    flag = 0
    for i in range(n):
        if abs(mas[i]) < y:
            asum = asum + mas[i]
        else:
            aprd = aprd * mas[i]
            flag = 1

    fo.write("Конечное состояние\n")
    for i in range(n):
        fo.write("{0: 7.3f}".format(mas[i]))
    fo.write("\n")
    if flag:
        fo.write("sum={0:7.3f} prd={1:7.3f}\n".format(asum, aprd))
    else:
        fo.write("sum={0:7.3f} prd=  нет элементов\n".format(asum))