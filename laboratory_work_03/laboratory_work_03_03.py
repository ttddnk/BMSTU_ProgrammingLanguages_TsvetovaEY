from math import *

print('Введите Xbeg, Xend, Dx и Eps')
xb = float(input('Xbeg='))
xe = float(input('Xend='))
dx = float(input('Dx='))
eps = float(input('Eps='))
print("+--------+--------+-----+")
print("I X I Y I N I")
print("+--------+--------+-----+")
xt = xb

y = int((xe - xb) / dx)
for i in range(y + 1):
    x = xb + i*dx
    n, y = 1, 1
    k, cnt = 0, 1
    while abs(n) >= eps and cnt < 100000:
        n *= -x * (k + 3)/(k + 1)
        y += n
        cnt += 1
    print("I{0: 7.2f} I{1: 7.3f} I{2: 4} I".format(xt, y, n))
    xt = xt + dx

print("+--------+--------+-----+")
