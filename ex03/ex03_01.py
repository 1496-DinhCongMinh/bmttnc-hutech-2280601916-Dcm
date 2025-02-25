def TongCacSoChan(a) :
    t = 0
    for i in a:
        if i%2==0:
            t=t+i
    return  t

inpu = input("Nhập vào danh sách các số cách nhau bởi dấu ,: ")
a = list(map(int , inpu.split(",")))

print(" Tổng các số chẵn có trong mảng: ", TongCacSoChan(a))