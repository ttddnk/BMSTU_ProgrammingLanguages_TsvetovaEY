from math import sqrt, log, tan, pi
with open("lab6_1_in.txt", "r") as fi, \
        open("lab6_1_ou.txt", "w") as fo:
    next(fi)
    line = fi.readline()
    (a, b) = line.split()
    a = float(a)
    b = float(b)

    fo.write("вариант 27\n")
    fo.write("z1 = a^sqrt(log_a(b)) - b^sqrt(log_b(a)) + tg(ab + 3pi/2)\n")
    fo.write("z2 = tg(ab + 3pi/2)\n")

    error = False
    if a <= 0:
        fo.write("должно быть > 0\n")
        error = True
    elif a == 1:
        fo.write("не должно равняться 1\n")
        error = True

    if b <= 0:
        fo.write("должно быть > 0\n")
        error = True
    elif b == 1:
        fo.write("не должно равняться 1\n")
        error = True
    if not error:
        log_ab = log(b, a)
        log_ba = log(a, b)

        if log_ab < 0 or log_ba < 0:
            fo.write("log_a(b) и log_b(a) должны быть >= 0\n")
            error = True
        else:
            arg_tg = a * b + 3 * pi / 2
            from math import cos
            if abs(cos(arg_tg)) < 1e-12:
                error = True

    if not error:
        z1 = a ** sqrt(log_ab) - b ** sqrt(log_ba) + tan(a * b + 3 * pi / 2)
        z2 = tan(a * b + 3 * pi / 2)

        fo.write("z1 = {:.6f}\n".format(z1))
        fo.write("z2 = {:.6f}\n".format(z2))