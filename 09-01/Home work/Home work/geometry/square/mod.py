# Создать переменную defaultSide,  не доступна при импорте и принимается функциями,
# если пользователь не предоставил свои размеры стороны квадрата.
__defaultSide = 5

# squarePerimeter() – вычисляет периметр квадрата,
def squarePerimeter(a):
	if a == '' or a is None:
		a =__defaultSide
	return a*4

# squareArea() – вычисляет площадь фигуры.
def squareArea(a):
	if a == '' or a is None:
		a =__defaultSide
	return a**2


