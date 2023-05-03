class GiaoDien_TuDien:
    def __init__(self) -> None:
        from TuDien import TuDien
        self.TuDien = TuDien()
        
    def InOption(self):
        print(
"""----------------------------------------
********TU DIEN TIENG ANH NHOM 8********
----------------------------------------
0. Thoat tu dien
1. Tra cuu tu
2. Tra cuu cau
3. Kiem tra tu vung
----------------------------------------"""
        )
        
    def LuaChon(self):
        match input('Nhap so: '):
            case '1':
                self.TuDien.TraCuuTu()
            case '2':
                self.TuDien.TraCuuCau()
            case '3':
                self.TuDien.KiemTraTuVung()
            case '0':
                self.repeat = False
                print('Bye!')
            case _:
                print('Vui long nhap lai')

        _ = input('Nhan phim ENTER...')
        
    def start(self):
        import os
        self.repeat = True
        while self.repeat:
            self.InOption()
            self.LuaChon()
            os.system('cls')
        