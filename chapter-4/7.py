my_tuple = (1, 5, 7, 9, 10, -100)
number = int(input("Nhap vao so can kiem tra"))
if number in my_tuple:
    print(f"{number} cos trong tuple")
else:
    print(f"{number} k cos trong tuple")