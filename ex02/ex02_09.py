import math


def ktngto(x):
    if x<2:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

z = int(input("Nhập số cần kt ngto: "))
if ktngto(z) :
    print(f" {z} Là số nguyên tố")
else :
    print(f"{z} không là số nguyên tố")