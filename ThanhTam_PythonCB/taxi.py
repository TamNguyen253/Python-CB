km = int(input('Nhập km: '))
tong = 0

if km < 1:
    print('Km ko hợp lệ')
elif km >= 1:
    tong = 20000
elif km >= 2 and km <= 5:
    tong = 20000 + (km - 1) * 16000
elif km >= 6 and km <= 10:
    tong = 20000 + 4 * 16000 + (km - 5) * 13000
elif km > 10:
    tong = 20000 + 4 * 16000 + 5 * 13000 + (km - 10) * 10000

if tong > 200000:
    tong -= 10 * 100

print(f'Tổng giá tiền: {tong}')
