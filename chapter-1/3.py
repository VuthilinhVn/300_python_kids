def check_max(a,b,c):
    if a>=b and a>=c:
        print(f"{a} is max number")
    elif b>=a and b>=c:
        print(f"{b} is max number")
    else:
        print(f"{c} is max number")

while True:
    try:
        a = int(input("a = "))
        b = int(input("b = "))
        c = int(input("c = "))
        check_max(a,b,c)
        break
    except ValueError:
        print("Invalid! Please try again! ")