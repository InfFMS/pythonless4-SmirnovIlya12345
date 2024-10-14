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
    a=0
    for i in range(0, round(log(num+1, 10)+0.5)):
        b=str(a)
        print(i)
        a+=int(b[-i-1])*(10**i)
    print(round(log(num+1, 10)+0.5), "ё")
    print(a)
    print(a*from_base)
convert_base(num, from_base, to_base)

