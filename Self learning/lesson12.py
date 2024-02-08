x = [10, 50, 68, 90, 56, 64, 188, 46, 200, 28]

'biến = list[start: end: step] là tạo 1 list khác và lấy các giá trị trong khoảng đó của list trước'
a = x[2: 5: 1]
print(a)

'lật ngược lại list nhưng không ảnh hưởng lên list đó'
b = x[::-1]
print(b)

'thay thế 1 phần tử trong list'
x[1: 2] = [100]
print(x)
x.pop(1)

'chèn phía trước list'
x[:0] = [1, 2, 3]
print(x)
del x[0: 3]

'chèn vào cuối của list'
x[len(x):] = [4, 5, 6]
print(x)
del x[10: 13]
print(x)

'chèn vào giữa của list'
'chỉ số các phần tử của list (hay số thứ tự các phần trong list) nó là kiểu giá trị nguyên nên' 
'nên vì thế a không thể dùng được vì nó là kiểu float'
a = len(x)/2
print(a) #--> 5.0
b = len(x)//2
print(b) #--> 5
x[len(x)//2: len(x)//2] = [70, 80]
print(x)                    

'lệnh copy 1 list nhanh'
c = x[:]
print(c)

'''tạo một danh sách ngẫu nhiên (list)'''
import random
def tao_danh_sach_ngau_nhien(kich_thuoc, pham_vi):
    return [random.randint(pham_vi[0], pham_vi[1]) for _ in range(kich_thuoc)]
# Sử dụng hàm để tạo một danh sách gồm 10 số ngẫu nhiên trong phạm vi từ 1 đến 100
danh_sach = tao_danh_sach_ngau_nhien(10, (1, 100))
print("Danh sách ngẫu nhiên:", danh_sach)