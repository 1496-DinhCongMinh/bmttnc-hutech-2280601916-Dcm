def dem_so_lam_xh(l):
    d = {}
    for i in l:
        if i in d:
            d[i] = d[i]+1
        else:
            d[i] = 1
    return d

s = input("Nhập vào danh sách các chuỗi , Cách nhau bởi dấu ,: ")
a = s.split(",")
d = dem_so_lam_xh(a)
print("Số lần xh: ", d)


