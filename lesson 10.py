"""[bài 8: chỉ cho phép người dùng chỉ nhập số nguyên có 5 chữ số]"""
while True:
    try:
        so_nguyen = int(input("Nhập số nguyên 5 chữ số: "))
        if 10000 <= so_nguyen <= 99999:
            print(f"Bạn đã nhập số nguyên hợp lệ: {so_nguyen}")
            break
        else:
            print("Vui lòng nhập số nguyên có đúng 5 chữ số.")
    except ValueError:
        print("Vui lòng nhập số nguyên.")

