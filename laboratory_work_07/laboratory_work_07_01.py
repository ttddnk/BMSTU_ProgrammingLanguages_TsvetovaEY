import turtle

K = 40
X_MIN, X_MAX = -8, 6
Y_MIN, Y_MAX = -5, 8
PAD = 30

def f(x):
    if x <= -2.5:
        y = -6/7*x - 36/7
    elif -2.5 <= x <= 2:
        y = (x + 2)*(x + 1)*(x - 1.5)
    else:
        y = -2*x + 10
    return y

screen = turtle.Screen()
screen.setup(width=(X_MAX - X_MIN)*K + 2*PAD, height=(Y_MAX - Y_MIN)*K + 2*PAD)
screen.setworldcoordinates(X_MIN*K - PAD, Y_MIN*K - PAD,X_MAX*K + PAD, Y_MAX*K + PAD)
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

def jump(x, y):
    t.penup()
    t.goto(x*K, y*K)
    t.pendown()

def line(x1, y1, x2, y2, color="black", width=1):
    t.color(color)
    t.pensize(width)
    jump(x1, y1)
    t.goto(x2*K, y2*K)

def label(x, y, text, size=9, align="center", color="black"):
    t.color(color)
    t.penup()
    t.goto(x*K, y*K)
    t.write(text, align=align, font=("Arial", size, "normal"))

for i in range(X_MIN, X_MAX + 1):
    line(i, Y_MIN, i, Y_MAX, "lightgray", 1)
for j in range(Y_MIN, Y_MAX + 1):
    line(X_MIN, j, X_MAX, j, "lightgray", 1)

line(X_MIN, 0, X_MAX, 0, "black", 2)
line(X_MAX, 0, X_MAX - 0.3, 0.12, "black", 2)
line(X_MAX, 0, X_MAX - 0.3, -0.12, "black", 2)
line(0, Y_MIN, 0, Y_MAX, "black", 2)
line(0, Y_MAX, 0.12, Y_MAX - 0.3, "black", 2)
line(0, Y_MAX, -0.12, Y_MAX - 0.3, "black", 2)
label(X_MAX - 0.2, -0.7, "x", 12)
label(0.4, Y_MAX - 0.6, "y", 12)

for i in range(X_MIN + 1, X_MAX):
    if i != 0:
        label(i, -0.6, str(i))
for j in range(Y_MIN + 1, Y_MAX):
    if j != 0:
        label(-0.15, j - 0.2, str(j), align="right")
label(-0.15, -0.6, "0", align="right")

t.color("red")
t.pensize(3)
x = X_MIN
jump(x, f(x))
while x <= X_MAX:
    t.goto(x*K, f(x)*K)
    x = round(x + 0.01, 2)

for xp in (-2.5, 2):
    t.penup()
    t.goto(xp*K, f(xp)*K)
    t.dot(8, "blue")
    label(xp + 0.1, f(xp) + 0.3, "({0}; {1:.0f})".format(xp, f(xp)), 9, "left", "blue")

label(-7.8, 2.5, "y = -6/7x - 36/7", 9, "left", "darkgreen")
label(-1.5, -4.6, "y = (x+2)(x+1)(x-1.5)", 9, "left", "darkgreen")
label(3.2, 5.5, "y = -2x + 10", 9, "left", "darkgreen")

screen.update()

if s:
    try:
        xv = float(s.replace(",", "."))
        yv = f(xv)
        print("вариант 27")
        print("X = {0:.2f} Y = {1:.2f}".format(xv, yv))
        if X_MIN <= xv <= X_MAX and Y_MIN <= yv <= Y_MAX:
            t.penup()
            t.goto(xv*K, yv*K)
            t.dot(10, "green")
            label(xv + 0.15, yv + 0.3, "({0:.2f}; {1:.2f})".format(xv, yv), 10, "left", "green")
            screen.update()
    except ValueError:
        print("Нужно ввести число")

turtle.done()
