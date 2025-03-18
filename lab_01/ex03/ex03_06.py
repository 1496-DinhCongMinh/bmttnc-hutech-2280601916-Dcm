def xoa_pt_the_key(d,k):
    if k in d:
        d.pop(k)
        return True
    return False

d = {'a':1,'b':2,'c':3,'d':4}

ptxoa = "m"
if xoa_pt_the_key(d,ptxoa) :
    print(f" Xóa pt key {ptxoa} thành coong: ", d)
else :
    print(f"Không tìm thấy pt key {ptxoa} trong ",d)

