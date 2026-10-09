from math import *
from random import *

n = int(input("Элементов в массиве(N<=30) N: "))
if n > 30:
    n = 30
elif n < 5:
    n = 5
print("Начальное состояние")
mas = []
for i in range(n):
    mas.append(uniform(-5, 5))
    print("{0: 7.3f}".format(mas[i]), end=" ")
amin = mas[0]
amax = mas[0]
for i in range(1, n):
    if mas[i] < amin:
        amin = mas[i]
    if mas[i] > amax:
        amax = mas[i]

print("amin={0:7.3f} amax={1:7.3f}".format(amin, amax))

y = float(input("Введите y (amin < y < amax): "))
while not (amin < y < amax):
    y = float(input("Неверно, повторите y: "))

asum = 0.0
aprd = 1.0
flag = 0
for i in range(n):
    if abs(mas[i]) < y:
        asum = asum + mas[i]
    else:
        aprd = aprd * mas[i]
        flag = 1

print("Конечное состояние")
for i in range(n):
    print("{0: 7.3f}".format(mas[i]), end=" ")
print()
if flag:
    print("sum={0:7.3f} prd={1:7.3f}".format(asum, aprd))
else:
    print("sum={0:7.3f} prd=  нет элементов".format(asum))