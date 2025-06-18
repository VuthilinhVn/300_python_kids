def is_prime(n):
    if n<=1:
        return False
    if n==3 or n==2:
        return True
    if n%2==0 or n%3==0:
        return False
    for i in range(5,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
        

while True:
    try:
        n = int(input("Nhap vao so n = "))
        if is_prime(n):
            print(f"{n} la so nguyen to")

        else:
            print(f"{n} khong phai so nguyen to")

        break
    except ValueError:
        print("Nhap vao so nguyen hop le!")


    