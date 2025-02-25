from SinhVien import SinhVien

class QuanLySinhVien:
    ds=[]

    def soLuongSinhVien(self):
        return len(self.ds)
    def XetHocLuc(self,dtb):
        if(dtb >=8):
            return "Giỏi"
        elif(dtb>=6.5):
            return "Khá"
        elif(dtb>=5):
            return "Trung Bình"
        else:
            return "Yếu"
    def timkiemtheoID(self, id):
        sv =None
        for i in self.ds:
            if i._id == id:
                sv = i
                break
        return sv

    def timkiemtheoTen(self, ten):
        dssv = []
        for i in self.ds:
            if ten.upper() in i._ten.upper() :
                dssv.append(i)
        return dssv


    def taoID(self):
        id  = 1
        if(self.soLuongSinhVien() > 0) :
            max = self.ds[0]._id
            for i in self.ds:
                if(max < i._id):
                    max = i._id
            id = id+max
        return id

    def themsinhvien(self):
        id = self.taoID()
        ten = input("Nhập tên sinh viên: ")
        gioitinh = input("Nhập giới tính sinh viên: ")
        chuyennganh = input("Nhập chuyên ngành sinh viên: ")
        dtb = float(input("Nhập điểm trung bình: "))
        sv = SinhVien(id,ten,gioitinh,chuyennganh,dtb)
        sv._hocluc = self.XetHocLuc(dtb)

        self.ds.append(sv)

    def capnhatsinhvien(self, id):
        sv:SinhVien = self.timkiemtheoID(id)
        if sv != None :
            sv._ten = input("Nhập tên sinh viên: ")
            sv._gioitinh = input("Nhập giới tính sinh viên: ")
            sv._chuyennganh = input("Nhập chuyên ngành sinh viên: ")
            sv._dtb = float(input("Nhập điểm trung bình: "))
            sv._hocluc = self.XetHocLuc(sv._dtb)
        else :
            print("Khống có sinh viên cần cập nhật")

    def xoasinhvientheoid(self, id):
        sv: SinhVien = self.timkiemtheoID(id)
        if sv != None:
            self.ds.remove(sv)
            return True
        return False

    def sxtheoDiem(self):
        self.ds.sort(key=lambda x: x._dtb, reverse=False)

    def sxtheoTenCN(self):
        self.ds.sort(key=lambda  x: x._chuyennganh, reverse=False)

    def dssinhvien(self , ds):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format("ID","Tên","Giới Tính","Chuyên Ngành","DTB","Học Lưc"))
        if(len(self.ds) > 0):
            for i in ds:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format(i._id,i._ten,i._gioitinh,i._chuyennganh,i._dtb,i._hocluc))

            print("\n")
    def getListSinhVien(self):
        return self.ds
