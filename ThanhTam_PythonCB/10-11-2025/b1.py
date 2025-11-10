try:
    So = int(float(input("Nhập số: ")))
except:
    print('Lỗi nhập liệu')
else:
    if So % 2 == 0:
        print(f'{So} là số chẵn')
    else:
        print(f'{So} là số lẽ')