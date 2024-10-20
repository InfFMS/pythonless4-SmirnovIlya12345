# Напишите функцию is_valid_triangle(side1, side2, side3),
# которая принимает в качестве аргументов три натуральных числа,
# и возвращает значение True, если существует невырожденный треугольник
# со сторонами side1, side2, side3, или False в противном случае.
side1=float(input())
side2=float(input())
side3=float(input())
def is_valid_triangle(side1, side2, side3):
    if max(side1,side2,side3)<(side1+side2+side3)/2 and min(side1, side2, side3)>0:
        return True
    else:
        return False
print(is_valid_triangle(side1, side2, side3))