'''[bài tập kiểu chuỗi]'''
x = "lop hoc python"
a = x.find('p',0,len(x))
b = x.find('p',a+1,len(x))
c = len(x)
d = x.replace(' ','')
e = x.count('p')
print('tìm chữ p đầu tiên có trong chuỗi:',a)
print('tìm chữ p tiếp theo có trong chuỗi:',b)
print('đếm số phần tử p có trong chuỗi:',c)
print('bỏ dấu cách trong chuỗi:',d)
print('số lượng p có trong chuỗi:',e)