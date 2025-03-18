def lay2ptdaucuoi(t):
    f = t[0]
    l = t[-1]
    return f,l

s = eval(input("nhập tuple: vd(1,2,3): "))
l,f = lay2ptdaucuoi(s)

print("PT ĐẦU: ",l)
print("PT CUỐI: ",f)