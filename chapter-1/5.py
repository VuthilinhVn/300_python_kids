def caculate_average(scores):
    return sum(scores)/len(scores)

def classification_average(average):
    if average >=8.5:
        return "Excelent"
    elif average >=7.0:
        return "Good"
    elif average >=5.5:
        return "Pair Good"
    elif average >=4.0:
        return "Average"
    else:
        return "Weak"
    
while True:
    try:
        subject_numbers = int(input("Nhap so luong mon hoc: "))
        scores = []
        if subject_numbers<=0:
            print("So luong mon hoc phai lon hon 0! ")
            continue
        else:
            for i in range(subject_numbers):
                score = float(input(f"Nhap so diem mon {i+1}: "))
                if score<0 or score>10:
                    print("Nhap diem khong hop le!")
                    break
                scores.append(score)
        if len(scores) == subject_numbers:
            average_score = caculate_average(scores)
            classification = classification_average(average_score)
            print(f"Diem trung binh = {average_score}, Xep loai {classification}")
            break
    except ValueError:
        print("Vui long nhap mot so hop le")

