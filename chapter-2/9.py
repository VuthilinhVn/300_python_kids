import math

def chuvi_dientich_circle(r):
    chuvi = 2*math.pi*r
    dientich = math.pi*(r**2)
    return chuvi, dientich

while True:
    try:

        r = float(input("Ban kinh hinh tron la: "))
        if r <=0:
            print("Banh kinh k the la so am, moi nhap lai!")
            continue
        else:
            chuvi, dientich = chuvi_dientich_circle(r)
            print(f"Chu vi cua hinh tron r = {r} la : {chuvi}")
            print(f"Dien tich cua hinh tron r = {r} la : {dientich}")
            break

    except ValueError:
        print("Moi nhap lai ban kinh hop le!")
