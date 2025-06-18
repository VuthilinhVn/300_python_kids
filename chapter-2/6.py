def is_palindrome(s):
    s2 = ""
    for i in s:
        s2 = i+s2
    if s2==s:
        return True
    else:
        False


s = input("Nhap string tu ban phim: ")
s_lower = s.lower()
if is_palindrome(s_lower):
    print(f"{s} la chuoi palindrome")

else:
    print(f"{s} khong phai chuoi palidrome")
