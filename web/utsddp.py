x = 2 ** 4
y = 5 // 2.0
print(x - y)
a = 3
b = 'fun'
c = 10
d = 5.0
not(c<d)
len(b)>0 and c-d<a
a*d<=c
a>c or len(b)<d
print("good\nnight\thow/nis/nit\nthis\\night")
a = input("nilai : ")
b = int(input("nilai : "))
print(a * b)
str = "bunga"
print(str * 3*2)
a = 2
b = 2
c = 4
m = 0
if a > b:
    if a > c:
         m = 1
    else:
        m = 2
else:
    if c != 0:
        m = 3
    else:
        m = 4
print(m)
x = 0
a = 9
b = 12
if a > 0:
    if b < 0:
        x = x + 5
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:     
    x = x + 2
print(x)
x = int(input("nilai : "))
if x > 2:
    x = x * 2
if x > 4:
    x = 0
print(x)
for i in range(2, 14, 3):
       p = i ** 2
       if p % 2 == 0:
           m = p // 2
print(m)
for i in range(10):
    if i % 2 == 0 and i % 3 == 0:
        continue
print(i)
x = 0
for i in range(5):
      for j in range(-1, -5, -1):
           x = x + 1
print(x)
x = 0
for i in range(1,3):
    for j in range(3,5):
        if j % i == 0:
            x = x + 1
print(x)
x = 8
y = 0
while y < x:
    y = y + 7
print(y)
stop = False
while stop == False:
    print("Hello World!")
    stop = True
print(stop)
i = -10
j = 1
while i < 0:
    i = i + j
    j = j + 1
print(j)
def square(x):
    x = x * x
    print(x)
    return x

x = 3
print(x)
print(square(x))
print(x)
def f(num1, num2=4):
    res = num1 * num2
    print(res)

f(7, 5)
def rec(n):
    print(1)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rec(n-1) + rec(n-2)
rec(4)
def rec(a, b):
    if b == 1:
        return a
    else:
        return a + rec(a, b-1)

print(rec(8,3))
x = 2 ** 3 ** 2 * 2
print(x)



