'''[cho biết số thuộc hàng nào]'''
num = int(input("nhập ba chữ số:"))
a = num//100
b = (num-100*a)//10
c = (num-100*a-10*b)
print('hàng trăm', a)
print('hàng chục', b)
print('đơn vị', c)