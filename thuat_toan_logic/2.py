import math


def cal_sigmoid(x):
    return 1/(1+math.exp(-x))

def cal_relu(x):
    if x<=0:
        return 0
    else:
        return x
    
def cal_elu(x):
    alpha = 0.01
    if x<=0:
        return (alpha*(math.exp(x)-1))
    else:
        return x

while True:
    try:
        activation_name = str(input("Moi nhap ten ham kich hoat: "))
        activation_name = activation_name.lower()
        x = int(input("Moi nhap gia tri x = "))
        if activation_name=="sigmoid":
            print(f"Sigmoid({x}) = {cal_sigmoid(x)}")
            break
        elif activation_name=="relu":
            print(f"ReLU({x}) = {cal_relu(x)}")
            break
        elif activation_name=="elu":
            print(f"ELU({x}) = {cal_elu(x)}")
            break
        else:
            print("Ham kich hoat khong hop le")
            continue
    except ValueError:
        print("x must be integer!")


