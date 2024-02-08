'''tập hợp các số chẵn từ 0 -> 100'''
while False:
    x = range(0, 101, 2)
    for i in x:
        print(i, end = ' ')


'''tính tổng của 1 dãy n'''
while False:
    n = int(input('tính tổng của bao nhiêu số đầu tiên: '))
    s = 0
    for i in range(0, n + 1, 1):
        s += i
    print(s)


'''tính tổng của 1 dãy n bình phương'''
while False:
    n = int(input('tính tổng của bao nhiêu số đầu tiên: '))
    s = 0
    for i in range(0, n + 1, 1):
        s += i**2
    print(s)


'''tạo vòng n lặp'''
while False:
    for i in range(1,7):
        print(i)
        i += 1


'''số chia hết cho 7 đầu tiên từ 0 -> n'''
while False:
    n = int(input('tới số: '))
    for i in range(1, n + 1, 1):
        print(i, end = ' ')
    print('xin lỗi')
    if i % 7 == 0:
        break   


'''cho thấy lệnh continue sẽ khiến cho các lệnh dưới nó ko đc thực hiện'''
while False:
    for i in range(1, 4, 1):
        print(i, 'hello')
        continue
        print('world')


'''đánh số mục lục như tiểu luận'''
while False:
    for i in range(1, 6, 1):
        print(i)
        for j in range(1, 4, 1):
            print(i, j, sep = '.')
            for k in range(1, 3, 1):
                print(i, j, k, sep = '.')


'''hàm ngay lỗi'''
while False:
    for i in range(1, 10, 0):
        print(i)


'''x = range(1, 10, 1) chạy ko được vì lệnh range chỉ dùng được bên trong vòng lặp for
print(x, end = ' ')'''


'''tính giai thừa của số n'''
while False:
    n = int(input('tính giai thừa của n = '))
    s = 1
    for i in range(1, n +1, 1):
        s *= i
    print(s)