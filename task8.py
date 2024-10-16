# Напишите рекурсивную функцию, которая
# раскладывает натуральное число на простые сомножители.
#
# Пример:
# Ввод:
# 378
# Вывод:
# 2*3*3*3*7
b=int(input())
from math import sqrt
a=[]
for i in range(2, b):
    c=0
    for j in range(2, int(round(sqrt(i)+0,5)+1)):
        if i%j==0:
            c+=1
            break
    if c==0:
        a.append(i)
c=[]
for i in range(0, len(a)):
    if b%a[i]==0:
            c.append(a[i])
            b=b/a[i]
    if b%a[i]==0:
            c.append(a[i])
            b=b/a[i]
    if b%a[i]==0:
            c.append(a[i])
            b=b/a[i]
    if b%a[i]==0:
            c.append(a[i])
            b=b/a[i]
    if b%a[i]==0:
            c.append(a[i])
            b=b/a[i]
    if b%a[i]==0:
            c.append(a[i])
            b=b/a[i]
    if b%a[i]==0:
            c.append(a[i])
            b=b/a[i]
    if b%a[i]==0:
            c.append(a[i])
            b=b/a[i]
    if b%a[i]==0:
            c.append(a[i])
            b=b/a[i]
    if b%a[i]==0:
            c.append(a[i])
            b=b/a[i]
print(c)
