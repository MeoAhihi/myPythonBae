class TuDien:
    def __init__(self) -> None:
        with open('file data.txt', 'r', encoding='utf-8') as TuDien:
            NoiDungTuDien = TuDien.read()

        self.TuDien = {}
        for Tu in NoiDungTuDien.split('-'):
            data = Tu.split(',')
            self.TuDien[data[0]] = (data[1], data[2])
    
    def __TraCuuTu(self, TuCanTra: str):
        try:
            return self.TuDien[TuCanTra]
        except KeyError:
            return False
    
    def __TraNghiaTu(self, TuCanTra: str):
        try:
            return self.TuDien[TuCanTra][1]
        except KeyError:
            return False
        
    def TraCuuTu(self):
        TuCanTraCuu = input('Tu can tra cuu: ')
        KetQua = self.__TraCuuTu(TuCanTraCuu)
        if KetQua:
            print('Loai tu la:', KetQua[0])
            print('Nghia la:', KetQua[1])
        else:
            print('Tu chua biet!')
            
    def TraCuuCau(self):
        CauCanTraCuu = input('Cau can tra cuu: ')
        NghiaCuaCau = []
        for Tu in CauCanTraCuu.split(' '):
            KetQua = self.__TraNghiaTu(Tu)
            if KetQua:
                NghiaCuaCau.append(KetQua)
            else:
                NghiaCuaCau.append('<unknown>')
        print('Nghia cua cau la: ' + " ".join(NghiaCuaCau))
        
    def KiemTraTuVung(self):
        from random import choice
        TuDuocChon = choice(list(self.TuDien))
        KetQua = self.__TraCuuTu(TuDuocChon)
        nghia = input('Nghia cua tu \'' + TuDuocChon + '\' la: ')
        if nghia == KetQua[1]:
            print('Chuc mung!')
        else:
            print(f'Nghia cua tu {TuDuocChon+KetQua[0]} la {KetQua[1]}')
