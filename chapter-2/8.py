def convert_C_to_F(C):
    F = ((C*9)/5)+32
    return F

C = float(input("Nhap vao do C: "))
F = convert_C_to_F(C)
print(f"{C} do C <-> {F} do F")