# Дано натуральное число N. Выведите слово YES,
# если число N является точной степенью двойки,
# или слово NO в противном случае.
# Операцией возведения в степень пользоваться нельзя!
# Задача на рекурсию!
from math import log2
a=int(input())
if log2(a)%1==0:
    print("YES")
else:
    print("NO")

