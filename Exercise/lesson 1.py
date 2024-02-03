'''[nhập các bài toán số vào code]'''
import math
x = float(input('x='))
a = abs((2 * math.pi * x-1) / (2 * math.pi * x ** 2))
# chạy được
b = 1 / (2 * math.pi * math.sqrt(math.sin(math.radians(x))))
# chạy được
c = math.sqrt(5 + math.cos(4 * x)) / abs(math.sin(3 * x))
# không chạy được
d = (math.e ** math.sin(math.radians(x))) / (2 * math.pi * math.sqrt(x ** 2 - 1))
# chạy được
e = math.sin(1 / (2 * math.pi * math.sqrt(x)))
# chạy được
print(a)
print(b)
print(c)
print(d)
print(e)