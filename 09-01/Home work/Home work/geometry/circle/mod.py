from math import pi

# Завести переменную defaultRadius, которая будет скрыта при импорте модуля.
__defaultRadius__ = 10
# Ее назначение – дефолтный радиус для окружности, если пользователь не введет свой

# circlePerimeter() – вычисляет длину окружности
def circlePerimeter(r):
	if r == '' or r is None:
		r = __defaultRadius__
	return 2 * pi * r

#  circleArea() – вычисляет площадь окружности.
def circleArea(r):
	if r == '' or r is None:
		r = __defaultRadius__
	return pi * r**2

