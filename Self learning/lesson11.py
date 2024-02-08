a = [1, 4, 6, 8, 10, 2]
for i in range(0, len(a), 1):
    print(i, end = ' ')


for j in a:
    print(j, end = ' ')

'tạo 1 list có 1 chữ số'
t = list(range(1, 101, 1))
print(t)


x = [1, 2.3, 'Hello', 2 - 5j, 1, 5, 6, 1]
y = [10244, 5, 4303, 100, 40]


x.remove(1)
print(x)


a = sorted(y)
print(a)


b = all(x)
print(b)


c = x.copy()
print(x == c)
print(x is c)
z = x
print(z == c) 
print(z is c)


d = y.count(6)
print(d)


e = x.count(1)
print(e)


f = x + y
print(f)
g = x.extend(y)
print(x)
print(g is f)
print(g == f)


x.reverse()
print(x)
v = x[::-1]
print(v)


y.sort()
print(y)


h = any(y)
print(h)


i = max(y)
print(i)


j = min(y)
print(j)


k = sum(y)
print(k)


print(x.index(1))