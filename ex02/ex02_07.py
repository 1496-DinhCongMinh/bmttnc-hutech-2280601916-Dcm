lines =[]
print("Nhập các dòng nhấn done đẻ kết thúc: ")
while True:
    line = input()
    if line.lower() == 'done' :
        break
    lines.append(line)
print("Các dòng đã nhập in hoa: ")
for i in lines :
    print(i.upper())