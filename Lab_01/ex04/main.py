from QuanLySinhVien import QuanLySinhVien


def hien_thi_menu():
    print("\n========== QUẢN LÝ SINH VIÊN ==========")
    print("1. Thêm sinh viên")
    print("2. Cập nhật thông tin sinh viên theo ID")
    print("3. Xóa sinh viên theo ID")
    print("4. Tìm kiếm sinh viên theo tên")
    print("5. Sắp xếp sinh viên theo điểm trung bình")
    print("6. Sắp xếp sinh viên theo tên chuyên ngành")
    print("7. Hiển thị danh sách sinh viên")
    print("0. Thoát")
    print("========================================")


def main():
    qlsv = QuanLySinhVien()

    while True:
        hien_thi_menu()
        lua_chon = input("Nhập lựa chọn: ")

        if lua_chon == "1":
            qlsv.them_sinh_vien()
        elif lua_chon == "2":
            qlsv.cap_nhat_sinh_vien()
        elif lua_chon == "3":
            qlsv.xoa_sinh_vien()
        elif lua_chon == "4":
            qlsv.tim_kiem_theo_ten()
        elif lua_chon == "5":
            qlsv.sap_xep_theo_diem()
        elif lua_chon == "6":
            qlsv.sap_xep_theo_chuyen_nganh()
        elif lua_chon == "7":
            qlsv.hien_thi_danh_sach()
        elif lua_chon == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")


if __name__ == "__main__":
    main()