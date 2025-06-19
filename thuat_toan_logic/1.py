def cal_F1(tp, fp, fn):
    Pre = tp/(tp+fp)
    recall = tp/(tp+fn)

    F1 = (2*(Pre*recall))/(Pre+recall)

    return Pre, recall, F1

while True:
    try:
        tp = int(input("Moi nhao gia tri TP = "))
        fp = int(input("Moi nhap gia tri FP = "))
        fn = int(input("Moi nhap gia tri FN = "))
        if tp>0 and fp>0 and fn>0:
            Pre, recall, F1 = cal_F1(tp,fp,fn)
            print(f"Precision = {Pre}, Recall = {recall}, F1-Score = {F1}")
            break
        else:
            print(" TP, FP, FN must be gather than zero!")
            continue
    except ValueError:
        print("TP,FP,FN must be a integer! ")