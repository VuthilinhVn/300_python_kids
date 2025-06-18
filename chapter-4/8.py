my_tuple = (0, 1, 5, 6, 9)

number = int(input("Phan tu can dem so lan xuat hien la: "))

if number in my_tuple:
    number_count = my_tuple.count(number)
    print(f"So lan xuat hien cua {number} trong tuple la : {number_count}")
else:
    print(f"{number} k ton tai trong tuple")