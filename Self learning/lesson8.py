'''tạo n vòng lặp'''
x = int(input('số vòng lặp muốn tạo thành: '))
n = 0
while n < x:
    n += 1
    print(n)


'''vòng lặp cho người chỉ nhập số dương lớn hơn 0'''
while True:
    n = int(input('nhập vào một số luôn dương và lớn hơn 0: '))
    if n > 0:
        break


'''đếm các chữ số có trong số cách 1'''
n = int(input('nhập vào một số: '))
x = 0
while n != 0:
    x += 1
    n //= 10
    print(x)    


'''đếm các chữ số có trong số cách 2'''
n = input('nhập vào 1 số: ')
print(len(n))


'''đảo nghịch số lại'''
n = int(input('nhập vào một số: '))
x = 0
while n != 0 :
    x = x * 10 + n % 10
    n //= 10
    print(x)    