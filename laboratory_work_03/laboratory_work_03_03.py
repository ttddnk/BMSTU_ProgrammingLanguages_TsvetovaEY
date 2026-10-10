from math import *
print("вариант 27")
print('Введите Xbeg, Xend, Dx и Eps')
xb = float(input('Xbeg='))
xe = float(input('Xend='))
dx = float(input('Dx='))
eps = float(input('Eps='))
print("+--------+--------+-----+")
print("I   X    I   Y    I  N  I")
print("+--------+--------+-----+")
xt = xb

y = int((xe - xb) / dx)
for i in range(y + 1):
    x = xb + i*dx
    n = 0
    a = 1.0
    y = a
    while abs(a) >= eps and n < 100000:
        n += 1
        a *= -(n + 2) / n * x
        y += a
    print("I{0: 7.2f} I{1: 7.3f} I{2: 4} I".format(xt, y, n))
    xt = xt + dx

print("+--------+--------+-----+")