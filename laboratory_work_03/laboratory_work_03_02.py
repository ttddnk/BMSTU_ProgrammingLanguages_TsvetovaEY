from math import *
from random import *
print("вариант 27")
r = float(input('R='))
flag = False
print("    X       Y   Res")
print("-------------------")
for n in range(10):
    x = uniform(-1, 4)
    y = uniform(-1, 10)
    if (x <= 0) and (y >= 0) and (x**2 + y**2 <= r**2) and (y >= x + r):
        flag = True
    elif (x >= 0) and (y >= 0) and (x <= r) and (y <= r) and (x**2 + y**2 >= r**2):
        flag = True
    elif (x >= 0) and (y <= 0) and (x**2 + y**2 <= r**2):
        flag = True
    elif (x <= 0) and (y <= 0) and (x >= -r) and (y >= -r) and (x**2 + y**2 >= r**2):
        flag = True
    else:
        flag = False
    print("{0: 7.2f} {1: 7.2f}".format(x, y), end=' ')
    if flag:
        print("Yes")
    else:
        print("No")
