'bài stack frame'
def a():
    print('A')
def b():
    a() #đối với thằng a() này nó đã biến thành 1 câu lệnh thực hiện chứ ko còn là khai báo tên và biến nữa (statement)  
    print('B')


'tạo vòng lặp liên tục bởi đệ quy'
def A():
    print('A')
    A()


'test thử câu lệnh không có else'
def ss(n):
    if n > 1:
        return print('True')
    return print('False') #do thằng return khi nó thằng def được nhận giá trị của thằng return nào thì giá trị thằng return còn lại sẽ không được nhận


'''viết về số Fibonacc'''


if __name__ == '__main__':
    b()
    A()
    ss(1) 
    print('C')