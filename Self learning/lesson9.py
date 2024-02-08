'''cách tạo 1 hàm hoàn chỉnh'''
'def name(arugment): --> name: là chỗ đặt tên hàm, để khi cần sẽ ghi ra; arugment: là các biến được thêm vào để thực các công việc'
'    statement and v.v --> statement: là chỗ để thực hiện các bài toán tử, các công việc và in (print) 1 một giá trị nào đó'
'    return value --> value: là chỗ nhận các đáp án đã được thực hiện, trường hợp đặc biệt với ở trên dùng lệnh print thì ko cần return' 
    

'''hàm tính tổng TV'''
def tong(a, b):
    res = a + b
    return res


'''hàm name'''
def name(name):
    print('tên của bạn là: ', name)


'''hàm chia hết cho 3 và 5'''
def check(n):
    if n % 3 and n % 5:
        return True
    else:
        return False


'''hàm tổng và hiệu của 2 số cùng 1 lúc'''
def tonghieu(x, y):
    tong = x + y
    hieu = y - x
    return tong, hieu


'''hàm giai thừa của số n'''
def giai_thua(n):
    if n == 0:
        return 1
    else:
        return n * giai_thua(n-1)


if __name__ == '__main__' :
    
    '''cách sử dụng hàm tính tổng'''
    x, y = map(int, input('tính tổng hai số bất kì: ').split())
    print(tong(x, y))


    '''cách sử dụng hàm name'''
    name('Phạm Hà Văn')


    '''cách sử dụng hàm check'''
    n = int(input('nhập vào 1 số bất kì: '))
    if check(n):
        print('True')
    else:
        print('False')


    '''cách sử hàm tonghieu'''
    a, b = tonghieu(15, 29)
    print(a)
    print(b)


    '''cách sử dụng hàm giai thừa'''
    n = int(input('tính giai thừa của n = '))
    print("Giai thừa của", n, "là", giai_thua(n))