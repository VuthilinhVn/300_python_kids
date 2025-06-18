def find_max_number(lst):
    n = len(lst)
    if n==0:
        print("Danh sach empty k co so lon nhat!") 
    else:
        lst.sort()
        print(f"So lon nhat cua {lst} la {lst[-1]}")


while True:
    try:
        lst = []
        n = int(input("Nhap vao so phan tu cua lst = "))
        if n<0:
            print("So phan tu cua list k the am")
            continue
        for i in range(n):
            item = float(input(f"Nhap phan tu thu {i+1} cua lst: "))
            lst.append(item)

        result = find_max_number(lst)

        break
    except ValueError:
        print("Nhap so nguyen hop le! ")