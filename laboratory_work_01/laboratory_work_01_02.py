from math import sqrt, log, tan, pi
print("вариант 27")
print("z1 = a^sqrt(log_a(b)) - b^sqrt(log_b(a)) + tg(ab + 3pi/2)")
print("z2 = tg(ab + 3pi/2)")
a = float(input('a (a > 0, a != 1): '))
b = float(input('b (b > 0, b != 1): '))
error = False
if a <= 0:
    print("должно быть > 0")
    error = True
elif a == 1:
    print("не должно равняться 1")
    error = True

if b <= 0:
    print("должно быть > 0")
    error = True
elif b == 1:
    print("не должно равняться 1")
    error = True
if not error:
    log_ab = log(b, a)
    log_ba = log(a, b)

    if log_ab < 0 or log_ba < 0:
        print("log_a(b) и log_b(a) должны быть >= 0")
        error = True
    else:
        arg_tg = a * b + 3 * pi / 2
        from math import cos
        if abs(cos(arg_tg)) < 1e-12:
            error = True

if not error:
    z1 = a ** sqrt(log_ab) - b ** sqrt(log_ba) + tan(a * b + 3 * pi / 2)
    z2 = tan(a * b + 3 * pi / 2)

    print("z1 = {:.6f}".format(z1))
    print("z2 = {:.6f}".format(z2))
    #print("{:.2e}".format(abs(z1 - z2)))