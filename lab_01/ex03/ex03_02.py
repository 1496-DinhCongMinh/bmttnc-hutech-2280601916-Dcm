def daonguocmang(x):
    return x[::-1]

s = input("Nhập vào danh sách các số , Cachs nhau bởi dấu ,: ")
a = list(map(int, s.split(",")))

a_dao = daonguocmang(a)
print(" List sau khi đảo ngươc: ", a_dao)