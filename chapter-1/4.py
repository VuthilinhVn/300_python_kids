def compute_fee(km):
    if km <= 0:
        print("Số km không hợp lệ!")
        return None
    if km <= 1:
        return 10000 * km
    elif km <= 10:
        return 8500 * km
    else:
        return 7500 * km

while True:
    try:
        km = float(input("Nhập vào số km = "))
        result = compute_fee(km)
        if result is not None:
            print(f"Số tiền cần trả là: {result:.0f} VND")
            break
    except ValueError:
        print("❌ Nhập sai định dạng! Hãy nhập số nhé.")
