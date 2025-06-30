

while True:
    try:
        tp = int(input("Moi nhap tp = "))
        fp = int(input("Moi nhap fp = "))
        result = tp/(tp+fp)
    except ZeroDivisionError:
        result = "Error: Divison by zero is not allowed!"
    
    

