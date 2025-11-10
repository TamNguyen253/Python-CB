import math

a = float(input('Nhập cạnh a: '))
b = float(input('Nhập cạnh b: '))
c = float(input('Nhập cạnh c: '))

if a > 0 and b > 0 and c > 0:
    if a + b > c and b + c > a and a + c > b:
        print('3 cạnh trên có thể tạo thành tam giác')
        cv = a + b + c
        p = cv / 2
        dt = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print(f'Chu vi của tam giác: {cv}')
        print(f'Diện tích của tam giác: {dt}')
    else:
        print('3 cạnh trên ko thể tạo thành tam giác')
else:
    print('Nhập cạnh không hợp lệ')