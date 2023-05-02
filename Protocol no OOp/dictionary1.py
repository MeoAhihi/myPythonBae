with open('file data.txt', 'r', encoding='utf-8') as TuDien:
    NoiDungTuDien = TuDien.read()

TuDien = {}
for Tu in NoiDungTuDien.split('-'):
    data = Tu.split(',')
    TuDien[data[0]] = (data[1], data[2])

def TraCuuTu():
    TuCanTraCuu = input('Tu can tra cuu: ')
    try:
        KetQua = TuDien[TuCanTraCuu]
        print('Loai tu la:', KetQua[0])
        print('Nghia la:', KetQua[1])
    except KeyError:
        print('Tu chua biet!')
        
def TraCuuCau():
    CauCanTraCuu = input('Cau can tra cuu: ')
    NghiaCuaCau = []
    for Tu in CauCanTraCuu.split(' '):
        try:
            NghiaCuaCau.append(TuDien[Tu][1])
        except KeyError: 
            NghiaCuaCau.append('<unknown>')
    print('Nghia cua cau la: ' + " ".join(NghiaCuaCau))


def KiemTraTuVung():
    from random import choice
    TuDuocChon = choice(list(TuDien))
    nghia = input('Nghia cua tu \'' + TuDuocChon + '\' la: ')
    if nghia == TuDien[TuDuocChon][1]:
        print('Chuc mung!')
    else:
        print(f'Nghia cua tu {TuDuocChon+TuDien[TuDuocChon][0]} la {TuDien[TuDuocChon][1]}')


def ThoatTuDien():
    print('Cam on va hen gap lai')


def functionality(option):
    match option:
        case '1':
            TraCuuTu()
        case '2':
            TraCuuCau()
        case '3':
            KiemTraTuVung()
        case '0':
            ThoatTuDien()
        case _:
            print('Vui long nhap lai')

    _ = input('Nhan phim ENTER...')


while True:
    print("----------------------------------------")
    print('TU DIEN TIENG ANH NHOM 8'.center(40, '*'))
    print("----------------------------------------")
    print('0. Thoat tu dien')
    print('1. Tra cuu tu')
    print('2. Tra cuu cau')
    print('3. Kiem tra tu vung')
    print("----------------------------------------")

    option = input('Nhap so: ')
    functionality(option)

