s = input("Nhập vào danh sách các số , Cachs nhau bởi dấu ,: ")
a = list(map(int , s.split(",")))

t = tuple(a)

print("List :", a)
print("Tuple: ",t)