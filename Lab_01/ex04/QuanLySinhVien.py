from SinhVien import SinhVien


class QuanLySinhVien:
    def __init__(self):
        self.danh_sach_sinh_vien = []

    def them_sinh_vien(self):
        ten = input("Nhập tên sinh viên: ")
        gioi_tinh = input("Nhập giới tính: ")
        chuyen_nganh = input("Nhập chuyên ngành: ")
        diem_tb = float(input("Nhập điểm trung bình: "))

        sinh_vien = SinhVien(ten, gioi_tinh, chuyen_nganh, diem_tb)
        self.danh_sach_sinh_vien.append(sinh_vien)

        print("Thêm sinh viên thành công.")

    def tim_sinh_vien_theo_id(self, id_sv):
        for sinh_vien in self.danh_sach_sinh_vien:
            if sinh_vien.id == id_sv:
                return sinh_vien
        return None

    def cap_nhat_sinh_vien(self):
        id_sv = int(input("Nhập ID sinh viên cần cập nhật: "))
        sinh_vien = self.tim_sinh_vien_theo_id(id_sv)

        if sinh_vien is None:
            print("Không tìm thấy sinh viên.")
            return

        sinh_vien.ten = input("Nhập tên mới: ")
        sinh_vien.gioi_tinh = input("Nhập giới tính mới: ")
        sinh_vien.chuyen_nganh = input("Nhập chuyên ngành mới: ")
        sinh_vien.diem_tb = float(input("Nhập điểm trung bình mới: "))
        sinh_vien.hoc_luc = sinh_vien.xep_loai_hoc_luc()

        print("Cập nhật sinh viên thành công.")

    def xoa_sinh_vien(self):
        id_sv = int(input("Nhập ID sinh viên cần xóa: "))
        sinh_vien = self.tim_sinh_vien_theo_id(id_sv)

        if sinh_vien is None:
            print("Không tìm thấy sinh viên.")
            return

        self.danh_sach_sinh_vien.remove(sinh_vien)
        print("Xóa sinh viên thành công.")

    def tim_kiem_theo_ten(self):
        ten_can_tim = input("Nhập tên sinh viên cần tìm: ").lower()
        ket_qua = []

        for sinh_vien in self.danh_sach_sinh_vien:
            if ten_can_tim in sinh_vien.ten.lower():
                ket_qua.append(sinh_vien)

        if len(ket_qua) == 0:
            print("Không tìm thấy sinh viên.")
        else:
            self.hien_thi_tieu_de()
            for sinh_vien in ket_qua:
                sinh_vien.hien_thi_thong_tin()

    def sap_xep_theo_diem(self):
        self.danh_sach_sinh_vien.sort(key=lambda sv: sv.diem_tb, reverse=True)
        print("Đã sắp xếp sinh viên theo điểm trung bình giảm dần.")

    def sap_xep_theo_chuyen_nganh(self):
        self.danh_sach_sinh_vien.sort(key=lambda sv: sv.chuyen_nganh)
        print("Đã sắp xếp sinh viên theo chuyên ngành.")

    def hien_thi_tieu_de(self):
        print(
            f"{'ID':<5} "
            f"{'Tên':<25} "
            f"{'Giới tính':<10} "
            f"{'Chuyên ngành':<20} "
            f"{'Điểm TB':<10} "
            f"{'Học lực':<12}"
        )
        print("-" * 85)

    def hien_thi_danh_sach(self):
        if len(self.danh_sach_sinh_vien) == 0:
            print("Danh sách sinh viên trống.")
            return

        self.hien_thi_tieu_de()

        for sinh_vien in self.danh_sach_sinh_vien:
            sinh_vien.hien_thi_thong_tin()