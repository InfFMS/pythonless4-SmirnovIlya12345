# Напишите процедуру, которая выводит на экран
# запись переданного ей числа в римской системе счисления.
# Числа находятся в диапазоне [1, 3999]
# I - 1, V - 5, X - 10, L - 50, C  - 100, D - 500, M - 1000
# Пример:
# 2013
# MMXIII
d=input()
a=d+"Q"
b=len(a)
def roman(a):
    c=0
    for i in range(0, b):
        if a[i]=="I" and (a[i+1]=="V" or a[i+1]=="X"):
            c+=-1
        elif a[i]=="I":
            c+=1
        if a[i]=="V":
            c+=5
        if a[i]=="X" and (a[i+1]=="L" or a[i+1]=="C"):
            c+=-10
        elif a[i]=="X":
            c+=10
        if a[i]=="L":
            c+=50
        if a[i]=="C" and (a[i+1]=="D" or a[i+1]=="M"):
            c+=-100
        elif a[i]=="C":
            c+=100
        if a[i]=="D":
            c+=500
        if a[i]=="M":
            c+=1000
    print(c)
roman(a)