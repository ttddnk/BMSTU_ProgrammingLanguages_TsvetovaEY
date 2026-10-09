flag = False
print('Введите координаты X и Y для точки и R для радиуса:')
x = float(input('X='))
y = float(input('Y='))
r = float(input('R='))

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

print("Точка X={0: 6.2f} Y={1: 6.2f}".format(x, y), end=" ")
if flag:
    print("попадает", end=" ")
else:
    print("не попадает", end=" ")
print("в область.")