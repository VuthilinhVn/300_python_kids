def sum_of_digits(n):
    total = 0
    for i in range(len(n)):
        total += int(n[i])
    return total

while True:
    try:
        n = abs(int(input("Nhap vao so nguyen n = ")))
        m = str(n)
        result = sum_of_digits(m)
        print(f"{n} co tong cac chu so la: {result}")
        break
    except ValueError:
        print("Moi nhap so nguyen hop le!")