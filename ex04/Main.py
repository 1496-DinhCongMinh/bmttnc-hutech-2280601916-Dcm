from QuanLySinhVien import QuanLySinhVien
qlsv = QuanLySinhVien()

while True :
    print(" =================== QUẢN LÝ SINH VIÊN =====================")
    print(" ***********************************************************")
    print(" *      1. Thêm                                            *")
    print(" *      2. Sửa                                             *")
    print(" *      3. Xóa                                             *")
    print(" *      4. Tìm kiếm theo Tên                               *")
    print(" *      5. SX theo DTB                                     *")
    print(" *      6. SX theo Ten CN                                  *")
    print(" *      7. Hiển thị DSSV                                   *")
    print(" *      8. Thoát                                           *")
    print(" ***********************************************************")

    cv = int(input(" Nhập CV :"))
    if cv==1 :
        print(" Thêm Sinh Viên: ")
        qlsv.themsinhvien()
        print(" Thêm Sinh Viên Thành Công")
    if cv==2:
        print(" Cập Nhật Sinh Viên:  ")
        id = int(input(" Nhập ID Cập Nhật: "))
        qlsv.capnhatsinhvien(id)
    if cv==3:
        print(" Xóa Sinh Viên")
        if qlsv.soLuongSinhVien() > 0:
            id = int(input(" Nhập ID SV Cần Xóa: "))
            print(" Đã Xóa Thành Công SV: ", qlsv.xoasinhvientheoid(id))
        else :
            print(" Chưa Có SV")
    if cv==4:
        print(" Tìm Kiếm Sinh Viên Theo Tên")
        if qlsv.soLuongSinhVien() > 0:
            id = (input(" Nhập Tên SV Cần TK: "))
            l_ten = qlsv.timkiemtheoTen(id)
            print(" DSSV có tên cần tìm: ")
            qlsv.dssinhvien(l_ten)
        else:
            print(" Chưa Có SV")
    if cv==5:
        print(" SX Theo DTB")
        if qlsv.soLuongSinhVien() > 0:
             qlsv.sxtheoDiem()
             print(" DSSV sau khi sx theo DTB: " )
             qlsv.dssinhvien(qlsv.getListSinhVien())
        else:
            print(" Chưa Có SV")
    if cv==6:
        print(" SX Theo Tên CN ")
        if qlsv.soLuongSinhVien() > 0:
            qlsv.sxtheoTenCN()
            print(" DSSV sau khi sx theo Tên CN: " )
            qlsv.dssinhvien(qlsv.getListSinhVien())
        else:
            print(" Chưa Có SV")
    if cv == 7:
        if qlsv.soLuongSinhVien() >0:
            print(" Hiển Thị DS SV")
            qlsv.dssinhvien(qlsv.getListSinhVien())
        else :
            print(" Chưa Có SV")
    if cv==8 or cv==0 :
        break