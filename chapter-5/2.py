my_dict = {'name':'Vu Thi Linh', 'age': 27, 'major': 'Computer Science'}

while True:
    try:

        key = input("Nhap tu khoa can timf kiem: ")
        if key in my_dict.keys():
            print(my_dict[key])
            break
        else:
            print(f"Dictionary khong co tu khoa {key}")
            continue
    except ValueError:
        print("Nhap lai!")