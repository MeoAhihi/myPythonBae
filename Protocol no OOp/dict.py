from random import randint

with open('file data.txt', 'r') as TuDien:
    NoiDungTuDien = TuDien.read()
Tu = NoiDungTuDien.split('-')
listTu = []
listLoaiTu = []
listNghia = []
Cau = (0, 0, 0)
for i in range(len(Tu)):
    Cau = Tu[i].split(",")
    listTu.append(Cau[0])
    listLoaiTu.append(Cau[1])
    listNghia.append(Cau[2])


def TraCuuTu():
    TuCanTraCuu = input('Tu can tra cuu: ')
    i = 0
    while i < len(listTu) and listTu[i] != TuCanTraCuu:
        i += 1
    if i == len(listTu):
        print('<unknow>')
        return
    print('Loai tu la:', listLoaiTu[i])
    print('Nghia la:', listNghia[i])


def TraCuuCau():
    CauCanTraCuu = input('Cau can tra cuu: ')
    TuTrongCau = CauCanTraCuu.split(' ')
    NghiaCuaCau = []
    for tu in TuTrongCau:
        i = 0
        while i < len(listTu) and listTu[i] != tu:
            i += 1
            if i == len(listTu):
                NghiaCuaCau.append('<unknow>')
        NghiaCuaCau.append(listNghia[i])
    print('Nghia cua cau la: ' + " ".join(NghiaCuaCau))


def KiemTraTuVung():
    i = randint(0, len(Tu))
    nghia = input('Nghia cua tu \'' + listTu[i] + '\' la: ')
    if nghia == listNghia[i]:
        print('Chuc mung!')
    else:
        print(f'Nghia cua tu {listTu[i]} la {listNghia[i]}')
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
