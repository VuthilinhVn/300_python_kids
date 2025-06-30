from datetime import datetime


class HocSinh:
    def __init__(self, hoten, nam_sinh, diem_tb, dia_chi):
        self.hoten = hoten
        self.nam_sinh = nam_sinh
        self.diem_tb = diem_tb
        self.dia_chi = dia_chi

    def hien_thi_thong_tin(self):
        print(f"Hoc sinh ten: {self.hoten}")
        print(f"Nam sinh: {self.nam_sinh}")
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
    def tinh_tuoi(self):
        hien_tai = datetime.now()
        nam = hien_tai.year
        print(f"Tuoi: {nam - self.nam_sinh}")


hocsinh_1 = HocSinh("vu thi linh", 1998, 8.5, "Viet Nam")
hocsinh_2 = HocSinh("Nguyen van A", 2000, 5.5, "Thai Nguyen")
hocsinh_3 = HocSinh("Tran thi B", 2003, 3.0, "Thai Nguyen 2")

hocsinh_lst = [hocsinh_1, hocsinh_2, hocsinh_3]
for student in range(len(hocsinh_lst)):

    hocsinh_lst[student].hien_thi_thong_tin()
    hocsinh_lst[student].tinh_tuoi()
    hocsinh_lst[student].xep_loai()
    print()