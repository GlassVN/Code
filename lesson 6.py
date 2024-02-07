'''[bài 5 cách 2]'''
chuoi_so = input("Nhập chuỗi số nguyên, phân cách bằng dấu cách: ")
# Chuyển chuỗi số thành danh sách các số nguyên
danh_sach_so = list(map(int, chuoi_so.split()))
# Tính tổng các phần tử
tong = sum(danh_sach_so)
# Tìm phần tử lớn nhất
phanele_lon_nhat = max(danh_sach_so)
print(f"Tổng các phần tử: {tong}")
print(f"Phần tử lớn nhất: {phanele_lon_nhat}")

