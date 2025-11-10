import math

a = float(input('Nhập a: '))
b = float(input('Nhập b: '))
c = float(input('Nhập c: '))
d = b * b - 4 * a * c

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print('Pt có 2 nghiệm pb:\n' \
    f'x1 = {x1} \nx2 = {x2}')
elif d == 0:
    x = -b / (2 * a)
    print('Pt có nghiệm kép:\n'f'x = {x}')
else:
    print('Pt vô nghiệm')