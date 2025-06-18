def factorial_recursive(n):
    if n ==0 or n==1:
        return 1
    else:
        return n*factorial_recursive(n-1)

while True:
    try:
        n = int(input("Nhap so nguyen duong n = "))
        if n<0:
            print("Giai thua khong xac dinh voi so am")
            print("so nhap phai la nguyen duong")
            continue
        result = factorial_recursive(n)
        print(f"Giai thua cua {n} la: {result}")
        break
    except ValueError:
        print("Nhap so nguyen duong hop le! ")