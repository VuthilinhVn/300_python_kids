def power(base, exponent):
    result = 1
    for i in range(int(exponent)):
        result = base*result
    return result

base = float(input("Nhap vao co so: "))
exponent = float(input("nhap vao so mu: "))

result = power(base, exponent)
print(f" {base}^{exponent} = {result}")