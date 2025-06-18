def find_ucln(a,b):
    if b != 0:
        a, b = b, a%b
        return a
    else:
        return a

while True:
    try:
        number1 = int(input("Nhap so nguyen a = "))
        number2 = int(input("Nhap so nguyen b = "))
        ucln = find_ucln(number1,number2)
        print(f"UCLN cuar {number1}, {number2} la {ucln}")
        break
    except ValueError:
        print("Nhap so nguyen hop le! ")