a = int(123)
b = 123
c = int('123')
d = int(123.22)
'''e = int('123.22') thằng này nó sẽ hiểu dấu chấm là dấu ngăn giữa 2 câu của văn bản chứ không phải dấu thập phân nên nó không thể biến kiểu dữ liệu về int được'''
print(a+b+c+d)
f = float('123')
print(f)
g = float(123)
print(type(g))
print(bool(100 != 29)), print(100!=29)
print(bool(38 == 39)), print(38==39)
h = 293
k = 473
j = 293
print(h is k)
print(h is not k)
print(h is j)
print(h is not j)