def check_n(n):
    if n != 0:
        if n%2==0:
            print(f"{n} is so chan")
        elif n%2==1:
            print(f"{n} is so le")
    else:
        print(f"{n} is zero")

while True:
    try:
        number = int(input("Input number = "))
        check_n(number)
        break
    except ValueError:
        print("Invalid, please try again! ")