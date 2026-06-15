class SinhVien:
    id_tu_tang = 1

    def __init__(self, ten, gioi_tinh, chuyen_nganh, diem_tb):
        self.id = SinhVien.id_tu_tang
        SinhVien.id_tu_tang += 1

        self.ten = ten
        self.gioi_tinh = gioi_tinh
        self.chuyen_nganh = chuyen_nganh
        self.diem_tb = diem_tb
        self.hoc_luc = self.xep_loai_hoc_luc()

    def xep_loai_hoc_luc(self):
        if self.diem_tb >= 8:
            return "Giỏi"
        elif self.diem_tb >= 6.5:
            return "Khá"
        elif self.diem_tb >= 5:
            return "Trung bình"
        else:
            return "Yếu"

    def hien_thi_thong_tin(self):
        print(
            f"{self.id:<5} "
            f"{self.ten:<25} "
            f"{self.gioi_tinh:<10} "
            f"{self.chuyen_nganh:<20} "
            f"{self.diem_tb:<10} "
            f"{self.hoc_luc:<12}"
        )