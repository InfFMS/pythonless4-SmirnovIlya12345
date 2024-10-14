# Напишите функцию, которая находит
# наибольший общий делитель двух натуральных чисел
# На входе два числа, на выходе их НОД.
a=int(input())
b=int(input())
def gcd(a,b):
    c=0
    c=max(a,b)
    d=min(a,b)
    a=c
    b=d
    if a%b==0:
        print("НОД:", b)
    else:
        e=1
        for i in range(1, b//2+1):
            if a%i==0 and b%i==0:
                e=i
        print("НОД:", e)
gcd(a,b)