def chi_het_cho_5(x):
    np = int(x)
    if np%5==0 :
        return True
    return False

s = input("Chuỗi các số nhị phân ngăn cách nhau bở dấu ,: ")
np_list = s.split(",")
so_chiahet_5 = [i for i in np_list if chi_het_cho_5(i)]

if len(so_chiahet_5) > 0:
    print("Các số chia hết cho 5 là : ", (",".join(so_chiahet_5)))
else :
    print(" Ko có số nhị phân nào chia hết cho 5")
