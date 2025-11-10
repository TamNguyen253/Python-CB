try:
    thang = int(input('Nhập tháng: '))
except:
    print('lỗi nhập liệu')
else:
    match thang:
        case 1|3|5|7|8|10|12:
            print(f'Tháng {thang} có 31 ngày')
        case 4|6|9|11:
            print(f'Tháng {thang} có 30 ngày')
        case 2:
            print(f'Tháng {thang} có 28 ngày hoặc 29 ngày nếu là năm nhuận')
        case _:
            print('Nhập tháng ko hợp lệ')