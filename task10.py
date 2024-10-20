# Напишите функцию convert_base(num, from_base, to_base),
# которая переводит натуральное число num из системы
# счисления с основанием from_base в систему счисления
# с основанием to_base
# 2 ≤ to_base ≤ 36 ; 2 ≤ from_base ≤ 36
# На входе три числа num, from_base, to_base
# На выходе одно число - результат работы функции
# Подсказка (если не получается решить):
# Попробуйте разбить задачу на две подзадачи:
# перевод из десятичной системы счисления в любую
# перевод из любой системы счисления в десятичную
# Объедините эти две подзадачи, получите ответ.
from math import log
num = (int(input()))
from_base = (int(input()))
to_base = (int(input()))
def convert_base(num, from_base, to_base):
    c=0
    e=len(str(num))
    for i in range(0, e):
        b=str(num)
        c+=int(b[i])*(from_base**(e-i-1))
    print(c)
    f=round(log(c, to_base)+0.5)
    h=0
    for i in range(0, f):
        print(c//(3**(f-i-1)))
        h+=(c//(3**(f-i-1)))*(10**(f-i-1))
        print(h, "h")
        c=c-h/((10**(f-i-1)))*(to_base**(f-i-1))
        print(c, "с")
    print(h)
convert_base(num, from_base, to_base)

