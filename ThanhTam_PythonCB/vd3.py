import math

r = float(input('nhập bán kính hình tròn: '))
cv = 2 * math.pi * r
dt = math.pi * (r ** 2)
print(f'chu vi hình tròn: {cv}')
print(f'diện tích hình tròn: {dt}')