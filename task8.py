# Напишите рекурсивную функцию, которая
# раскладывает натуральное число на простые сомножители.
#
# Пример:
# Ввод:
# 378
# Вывод:
# 2*3*3*3*7
a = []
b = int(input())
for i in range(2, b + 1):
    c = 0
    for j in range(2, round(i * 0.5 + 1)):
        if i % j == 0:
            c += 1
            break
    if c == 0:
        a.append(i)
d=[]
def prime_factors(b):
    for j in range(0, len(a)):
        if b==1:
            return True
        if b%a[j]==0:
            b=b/a[j]
            d.append(a[j])
            return prime_factors(b)
prime_factors(b)
e=""
for k in range(len(d)):
    e=e+str(d[k])
    if k!=len(d)-1:
        e=e+"*"
print(e)
