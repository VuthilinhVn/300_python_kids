import math

def chuvi_dientich_hcn(width, length):
    chuvi = 2*(width+length)
    dientich = width * length
    return chuvi, dientich

while True:
    try:
        width = float(input("chieu rong hcn: "))
        length = float(input("chieu dai hcn: "))
        if width<=0 or length<=0:
            print("Thong so hcn sai, moi nhap lai!")
            continue
        else:
            chuvi, dientich = chuvi_dientich_hcn(width, length)
            print(f"chu vi hcn {length}x{width} la : {chuvi}")
            print(f"Dien tich cua hcn {length}x{width} la : {dientich}")
            break

    except ValueError:
        print("Moi nhap lai thong so hop le")
