from math import sqrt

# Создать три переменные (длины сторон треугольника): a, b и c, которые также не будут видны при импорте, используются если пользователь ничего не введет.
__a = 5
__b = 5
__c = 5
# На вход функциям передается длина трех.

# trianglePerimeter() – вычисляет периметр треугольника
def trianglePerimeter(a,b,c):
	if a == '' or a is None:
		a = __a
	if b == '' or b is None:
		b = __b
	if c == '' or c is None:
		c = __c
	return a+b+c

# triangleArea() – вычисляет площадь фигуры.
def triangleArea(a,b,c):
	if a == '' or a is None:
		a = __a
	if b == '' or b is None:
		b = __b
	if c == '' or c is None:
		c = __c
	p = trianglePerimeter(a,b,c)
	return sqrt(p * (p-a) * (p-b) * (p-c))

