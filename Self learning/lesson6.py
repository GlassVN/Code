'''cho một số n bất kì có thuộc đoạn [10, 100] hay nhập số có hai chữ số'''
while False:
    n = int(input('nhập vào 1 số:'))
    if (n >= 10) and (n <= 100):
        print('True')


'''kiểm tra một số bất kì có thuộc một đoạn bất kì hay không'''
while False:
    x, y = map(int, input('nhập vào 2 cận:').split())
    z = int(input('nhập vào số cần kiểm tra:'))
    if (z >= x) and (z <= y):
        print(z, 'thuộc đoạn',f'[{x}, {y}]')


'''kiểm coi tháng đó có bao nhiêu ngày'''
while False:
    t = int(input('nhập vào một tháng bất kì \n t ='))
    if t == 1 or t == 3 or t == 5 or t == 7 or t == 8 or t == 10 or t == 12: print(f'tháng {t} có 31 ngày')
    elif t == 4 or t == 6 or t == 9 or t ==  11 : print(f'tháng {t} có 30 ngày')
    elif t == 2 : print(f'tháng {t} có 28 hoặc 29 ngày')
    else : print('dữ liệu không tồn tại')


'''kiểm tra số lớn hơn hay bé hơn'''
while False:
    a = int(input('a ='))
    b = int(input('b ='))
    c = 'bé hơn' if (a < b) else 'lớn hơn'
    print(f'{a}', c, f'{b}')


'''kiểm tra 1 số bất kì có lớn hơn 20 và chia hết cho 3 hoặc 5 hoặc 7 cách 1'''
while False:
    n = int(input('nhập vào 1 số bất kì:'))
    if n >= 20 and (n % 3 == 0 or n % 5 == 0 or n % 7 == 0): 
        print(n, 'thỏa mãn các điều kiện')
    else:
        print(n, 'không thỏa mãn các điều kiện')


'''kiểm tra 1 số bất kì có lớn hơn 20 và chia hết cho 3 hoặc 5 hoặc 7 cách 2'''
while False:
    n = int(input('nhập vào 1 số bất kì:'))
    if n >= 20:
        if(n % 3 == 0 or n % 5 == 0 or n % 7 == 0): 
            print(n, 'thỏa mãn các điều kiện')
        else:
            print(n, 'không thỏa mãn các điều kiện')


'''kiểm tra 1 số bất kì có lớn hơn 20 và chia hết cho 3 hoặc 5 hoặc 7 cách 3'''
while False:
    n = int(input('nhập vào 1 số bất kì:'))
    a = 'thỏa mãn các điều kiện' if ((n >= 20) and (n % 3 == 0 or n % 5 == 0 or n % 7 == 0)) else 'không thỏa mãn các điều kiện'
    print(f'{n}', a)