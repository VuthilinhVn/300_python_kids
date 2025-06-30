class HocSinh:
    def __init__(self, hoten, tuoi, diem_tb, dia_chi):
        self.hoten = hoten
        self.tuoi = tuoi
        self.diem_tb = diem_tb
        self.dia_chi = dia_chi

    def hien_thi_thong_tin(self):
        print(f"Hoc sinh ten: {self.hoten}")
        print(f"Tuoi: {self.tuoi}")
        print(f"Diem trung binh: {self.diem_tb}")
        print(f"Dia chi: {self.dia_chi}")
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
        
hocsinh = HocSinh("vu thi linh", 27, 8.5, "Viet nam")

hocsinh.hien_thi_thong_tin()

hocsinh.xep_loai()