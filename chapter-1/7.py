def check_year(year):
    if (year%4==0 and year%100==1) or year%400==0:
        print(f"{year} la nam nhuan")
    else:
        print(f"{year} khong phai nam nhuan")

while True:
    try:
        year = int(input("Nhap vao so nam: "))
        check_year(year)
        break
    except ValueError:
        print("Nam phai la so nguyen!")