class Machine:
	"""Описание класса"""
	def __init__(self, whell, type, doors, color):
		"""конструктор класса"""
		self.whell = whell
		self.type = type
		self.doors = doors
		self.color = color

	def drive(self):
		"""метод машина в движение"""
		return "Its driving"

	def brake(self):
		"""метод машина останавливается"""
		return "Its brakeing"


if __name__ == "__main__":
	teh1 = Machine(4, "car", 5, "red")
	teh2 = Machine(8, "truck", 2, "green")
	print(teh1.drive())
	print(teh1.brake())


def powof2(n):
	pow = 1
	for i in range(n):
		yield pow
		pow *= 2

def fib(n):
	if n <= 0:
		return None
	a = b = 1
	yield a
	for i in range(n):
		yield b
		a, b = b, a+b

def polinom(x):
	return 2 * x**2 + 4*x -2

pol = lambda x: 2 * x**2 +4*x -2

def genPol(funk, a = 0, b = 0):
	for i in range(a,b):
		yield funk(i)

# list1 = list(genPol(polinom,0, 10))
# print(list1)
#
# list2 = [pol(i) for i in range(0, 10)]
# print(list2)

import random

def sort(arr = []):
	srar = sum(arr) / len(arr)
	if srar > 0:
		d = int(len(arr) / 3 * 2)
	else:
		d = int(len(arr) / 3)
	arr1 = sorted(arr[: d])
	arr2 = list(reversed(arr[d:]))
	arr.clear()
	arr.extend(arr1 + arr2)



# list3 = [random.randint(1, 20) for i in range(10)]
# print(list3)
# sort(list3)
# print(list3)


def menu (menuString, arr, *tasks):
	print(menuString)
	while True:
		print(f"{len(tasks)+1}. Для повторного вывода меню")
		try:
			taskNum = int(input("Введите номер пункта меню: "))
			if taskNum < 0 or taskNum > len(tasks)+1:
				raise ValueError
		except:
			print("Значение не корректно!!!")
			continue
		if taskNum == 0:
			return
		elif taskNum == len(tasks)+1:
			print(menuString)
		else:
			tasks[taskNum-1](arr)

def task1(arr):
	while True:
		str = input("Введите 12 оценок, через пробел: ")
		str = str.split()
		try:
			arr.clear()
			arr.extend([int(num) for num in str])
		except:
			print("Значение не корректно!")
			continue
		break

def task2(arr):
	print(arr)

def task3(arr):
	while True:
		try:
			i = int(input("Введите номер оценки: "))
			value = int(input("Введите оценку: "))
			arr[i] = value
		except:
			print("Не корректное значение!")
			continue
		break

def task4(arr):
	if sum(arr) / len(arr) > 10.7:
		print("Степендия выходит!")
	else:
		print("Степендия не выходит :(")

def task5(arr):
	print(sorted(arr))


if __name__ == "__main__":
	menuStr = "1. Ввод оценок\n" \
			  "2. Вывод оценок\n" \
			  "3. Пересдача\n" \
			  "4. Выходит ли степендия?\n" \
			  "5. Вывод отсортированного списка"
	arr =[]
	menu(menuStr, arr, task1, task2, task3, task4, task5)