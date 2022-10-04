def printBox(arr):
	listNum = [str(i) for i in range(len(arr))]
	print("   "+"  ".join(listNum))
	for i in range(len(arr)):
		print(listNum[i], end="  ")
		print("  ".join(arr[i]))
	print("------///////------")

def add(arr,x,y,point):
	if arr[y][x] == " ":
		arr[y][x] = point
		return True
	else:
		print("Место занято!")
		return False

def statusGame(arr):
	# Проверка на ничью
	draw = True
	for i in range(len(arr)):
		if arr[i].count(" ") > 0:
			draw = False
			break
	if draw:
		return "draw"
	# Проверка по строчка
	for i in range(len(arr)):
		b = arr[i][0]
		for j in range(1,len(arr)):
			if b != arr[i][j]:
				b = ' '
				break
		if b != ' ':
			return b
	# Проверка по столбцам
	for i in range(len(arr)):
		b = arr[0][i]
		for j in range(1,len(arr)):
			if b != arr[j][i]:
				b = ' '
				break
		if b != ' ':
			return b
	# Проверка по 1 диагонали
	b = arr[0][0]
	for j in range(1, len(arr)):
		if b != arr[j][i]:
			b = ' '
			break
	if b != ' ':
		return b
	# Проверка по 2 диагонали
	b = arr[0][-1]
	for j in range(1, len(arr)):
		if b != arr[j][-j-1]:
			b = ' '
			break
	if b != ' ':
		return b
	return b

def userMove(box):
	print("Установите X:")
	while True:
		try:
			x = int(input("Введите Х: "))
			y = int(input("Введите Y: "))
		except Exception:
			print("Нужно вводить числа!")
			continue
		if x < 0 or x >= len(box) or y < 0 or y >= len(box):
			print(f"Числа могут быть от 0 до {len(box)-1}!")
			continue
		if add(box,x,y,"X"):
			break

def botMove(box, numStep):
	#В 1 ход занимаем лучшие места
	n = len(box)
	if numStep == 1:
		if box[int((n-1)/2)][int(n/2)] == ' ':
			box[int((n-1)/2)][int(n/2)] = '0'
		elif box[0][0] == ' ':
			box[0][0] = '0'
		elif box[0][-1] == ' ':
			box[0][-1] = '0'
		elif box[-1][0] == ' ':
			box[-1][0] = '0'
		elif box[-1][-1] == ' ':
			box[-1][-1] = '0'
	else:
		for i in range(n):
			for j in range(n):
				if box[i][j] == " ":
					box[i][j] = "0"
					if statusGame(box) == '0':
						return
					else:
						box[i][j] = " "
		for i in range(n):
			for j in range(n):
				if box[i][j] == " ":
					box[i][j] = "X"
					if statusGame(box) == 'X':
						box[i][j] = "0"
						return
					else:
						box[i][j] = " "
		if box[int((n-1)/2)][int(n/2)] == ' ':
			box[int((n-1)/2)][int(n/2)] = '0'
		elif box[0][0] == ' ':
			box[0][0] = '0'
		elif box[0][-1] == ' ':
			box[0][-1] = '0'
		elif box[-1][0] == ' ':
			box[-1][0] = '0'
		elif box[-1][-1] == ' ':
			box[-1][-1] = '0'
		else:
			for i in range(n):
				for j in range(n):
					if box[i][j] == ' ':
						box[i][j] = '0'
						return


#Основной код
print("Какое поле?")
while True:
	try:
		n = int(input("Введите n: "))
	except Exception:
		print("Данные введены не корректно. Попробуйте ещё раз.")
		continue
	break
box = [[" " for i in range(n)]for j in range(n)]
printBox(box)
numStep = 1
while True:
	userMove(box)
	if statusGame(box) != ' ':
		break
	botMove(box,numStep)
	if statusGame(box) != ' ':
		break
	printBox(box)
	numStep += 1

printBox(box)
if statusGame(box) == 'X':
	print("Вы победили!!!")
elif statusGame(box) == '0':
	print("БОТ вас дёрнул :)")
else:
	print("Ничья.")