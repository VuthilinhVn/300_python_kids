class HocSinh:
    def __init__(self, ten, tuoi, diem_tb, dia_chi):
        self.ten = ten  # thuoc tinh public
        self._tuoi = tuoi # thuoc tinh private (nhac dev rang cai nay k the dong vao, nhung van co the goi tu ben ngoai)
        self.diem_tb = diem_tb 
        self.__dia_chi = dia_chi # thuoc tinh private mangling ( thuc su private)

    def hien_thi(self):
        print(f"Hoc sinh: {self.ten}")
        print(f"Tuoi: {self._tuoi}")
        print(f"Diem tb: {self.diem_tb}")
        print(f"Dia chi: {self.__dia_chi}")

    def xep_loai(self):
        if self.diem_tb>=8.5:
            return "Excelent"
        elif self.diem_tb>=7.0:
            return "Good"
        elif self.diem_tb>=6.5:
            return "Fair Good"
        elif self.diem_tb>5.0:
            return "Average"
        else:
            return "Weak"

    @property
    def tuoi(self):
        return self._tuoi
    @tuoi.setter
    def tuoi(self, tuoi_moi):
        if tuoi_moi >0:
            self._tuoi = tuoi_moi
        else:
            print("Tuoi moi khong hop le!")
    def get_dia_chi(self):
        return self.__dia_chi
    def set_dia_chi(self, dia_chi_moi):
        self.__dia_chi = dia_chi_moi

hs = HocSinh("Vu thi linh", 27, 8.5, "123 duong A")
print(f"Truoc khi thay doi: Ten - {hs.ten}, Diem tb: {hs.diem_tb}, Tuoi: {hs.tuoi}, Dia chi: {hs.get_dia_chi()}")
hs.tuoi = 17
hs.ten = "Tran thi B"
hs.diem_tb = 7.0
hs.set_dia_chi("567 thanh pho B")
print(f"Sau khi thay doi: Ten - {hs.ten}, Tuoi: {hs.tuoi}, Diem tb: {hs.diem_tb}, Dia chi: {hs.get_dia_chi()}")
