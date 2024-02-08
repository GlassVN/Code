'''cách để biến đổi kiểu khi nhập dữ liệu trên cùng 1 dòng cách 1'''
while False:
    #cho chỗ để nhập giá trị vào
    x = input('nhập 3 số vào:')
    #tách một xâu lớn thành các xâu riêng biệt
    y = x.split()
    #sử dụng lệnh map để biến các xâu riêng biệt y thành một kiểu dữ liệu khác
    a, b, c = map(int, y)
    print(a + b - c)


'''cách để biến đổi kiểu khi nhập dữ liệu trên cùng 1 dòng cách 2'''
while False:
    a, b, c = map(int, input('nhập 3 số vào:').split())
    print(a + b + c)


'''cách biến đổi kiểu dữ liệu của 1 số và các số được nhập vào từng dòng'''
while False:
    n = int(input())
    x = str(n)
    print('kiểu dữ liệu của n', type (n))
    print('kiểu dữ liệu của x', type(x))


'''nhập 3 số cho vào thành 1 số và biến 3 số cho vào tạo thành mảng'''
while False:
    x = input('nhập 3 số vào:')
    y = x.split()
    a, b, c = y
    print(a + b + c)
    print(y)


'''lệnh giúp đỡ thư viện math'''
import math
print(help(math))