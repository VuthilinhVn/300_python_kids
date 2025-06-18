def check_number(lst):
    chan = []
    le = []
    for i in lst:
        if i%2==0:
            chan.append(i)
        if i%2==1:
            le.append(i)
    print(f"Cac so chan la: {chan}, Cac so le la: {le}")

while True:
   
    try:
        items = int(input("Nhap so phan tu cua list: "))

        if items<=0:
            print("Nhap so luong phan tu hop le!")
            continue
        lst = []
        for i in range(items):
            
            item = int(input(f"Nhap phan tu thu {i+1}: "))
            lst.append(item)

        check_number(lst)
        break
    except ValueError:
        print("Nhap gia tri hop le! ")

            