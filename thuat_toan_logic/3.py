






while True:
    try:
        num_sample = int(input("Moi nhap so luong mau num_sample = "))
        loss_name = str(input("Moi nhap loss name: "))
        loss_name = loss_name.lower()

        if loss_name=="mae":
            print()