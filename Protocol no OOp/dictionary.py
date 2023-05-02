with open('file data.txt', 'r', encoding='utf-8') as TuDien:
    NoiDungTuDien = TuDien.read()

TuDien = []
for Tu in NoiDungTuDien.split('-'):
    TuDien.append(tuple(Tu.split(',')))


def TraCuuTu():
    TuCanTraCuu = input('Tu can tra cuu: ')
    KetQua = [tu for tu in TuDien if tu[0] == TuCanTraCuu]
    if not KetQua:
        print('Tu chua biet!')
        return
    print('Loai tu la:', KetQua[0][1])
    print('Nghia la:', KetQua[0][2])


def TraCuuCau():
    CauCanTraCuu = input('Cau can tra cuu: ')
    TuTrongCau = CauCanTraCuu.split(' ')
    NghiaCuaCau = []
    for Tu in TuTrongCau:
        KetQua = [tu for tu in TuDien if tu[0] == Tu]
        if not KetQua:
            NghiaCuaCau.append('<unknown>')
        else:
            NghiaCuaCau.append(KetQua[0][2])
    print('Nghia cua cau la: ' + " ".join(NghiaCuaCau))


def KiemTraTuVung():
    from random import randint
    index = randint(0, len(TuDien)-1)
    TuDuocChon = TuDien[index]
    nghia = input('Nghia cua tu \'' + TuDuocChon[0] + '\' la: ')
    if nghia == TuDuocChon[2]:
        print('Chuc mung!')
    else:
        print(
            f'Nghia cua tu {TuDuocChon[0]+TuDuocChon[1]} la {TuDuocChon[2]}')
    print()


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

