
def sum_n(n):
    return (n*(n+1))/2


while True:
    try:
        n = int(input("Nhap so nguyen duong: "))
        if n<0:
            print("Phai nhap mot so nguyen duong! Moi nhap lai: ")
            continue
        result = sum_n(n)
        print(f"Sum(1->{n}) la : {result}")
        break
    except ValueError:
        print("Nhap vao khong hop le, Moi nhap lai! ")