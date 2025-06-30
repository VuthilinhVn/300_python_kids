class Student:
    def __init__(self, name, age, average_score):
        self.name = name
        self.age = age
        self.average_score = average_score
    
    def describe(self):
        print(f"Hoc sinh : {self.name}")
        print(f"Tuoi: {self.age}")
        print(f"Diem trung binh: {self.average_score}")

    def xep_loai(self):
        if self.average_score >= 8.5:
            return "Good"
        elif self.average_score >= 6.5:
            return "Fair good"
        elif self.average_score >= 5.0:
            return "Average"
        else:
            return "Weak"
        
hs = Student("Vu thi Linh", 27, 6.0)
hs.describe()
print(hs.xep_loai())
