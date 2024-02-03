'''[bài 7: giúp đọc số dễ dàng]'''
so_nguyen = int(input('nhập vào một số nguyên:'))
chuoi_so_1 = "{:,}".format(so_nguyen)
chuoi_so_2 = chuoi_so_1.replace(",",".") 
print(chuoi_so_1)
print(chuoi_so_2)