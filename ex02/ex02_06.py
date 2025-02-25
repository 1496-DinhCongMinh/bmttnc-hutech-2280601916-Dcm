input_str = input("Nhập X, Y: ")
a = input_str.split(",")
d = int(a[0])
c = int(a[1])
mt=[[0 for col in range(c)] for row in range(d)]
for i in range(0, d):
    for j in range(0, c):
        mt[i][j] = i*j

print(mt)