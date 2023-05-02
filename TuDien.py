class TuDien:
    def __init__(self) -> None:
        with open('file data.txt', 'r', encoding='utf-8') as TuDien:
            NoiDungTuDien = TuDien.read()

        self.TuDien = {}
        for Tu in NoiDungTuDien.split('-'):
            data = Tu.split(',')
            TuDien[data[0]] = (data[1], data[2])
    
    def __TraCuuTu(self, TuCanTra: str):
        try:
            return self.TuDien[TuCanTra]
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