thang = int(input('Nhập tháng: '))

match thang:
    case 2|3|4:
        print('Mùa Xuân')
    case 5|6|7:
        print('Mùa hạ')
    case 8|9|10:
        print('Mùa thu')
    case 11|12|1:
        print('Mùa đông')
    case _:
        print('Nhập tháng không phù hợp')
        