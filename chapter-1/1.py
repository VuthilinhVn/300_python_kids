def check_number(number):
    if number>0: 
        print(f"{number} is positive number")
    elif number<0:
        print(f"{number} is negative number")
    else:
        print(f"{number} is zero")

while True:
    try:
        number = int(input("Input number = "))
        check_number(number)
        break
    except ValueError:
        print("Invalid, please try again! ")
