class StartingValue:
	def __init__(self):
		while True:
			try:
				self.fieldSize = int(input("Введите размер поля (Значение от 3): "))
			except:
				print("Вы ввели не корректное значение. Попробуйте ещё раз.")
				continue
			if self.fieldSize < 3:
				print("Число должно быть больше 3-x. Повторите ввод.")
				continue
			break

		print("Введите стартовое положение коня. Точка отсчета координат находится в верхенем левом углу.\n"
			  "Строки и столбцы считаются от 0")
		while True:
			try:
				self.indStrHorse = int(input("Введите номер строки: "))
			except:
				print("Вы ввели не корректное значение. Попробуйте ещё раз.")
				continue
			if self.indStrHorse < 0 or self.indStrHorse >= self.fieldSize:
				print(f"Число должно быть больше 0 и меньше {self.fieldSize}. Повторите ввод.")
				continue
			break
		while True:
			try:
				self.indColumnHorse = int(input("Введите номер столбца: "))
			except:
				print("Вы ввели не корректное значение. Попробуйте ещё раз.")
				continue
			if self.indColumnHorse < 0 or self.indColumnHorse >= self.fieldSize:
				print(f"Число должно быть больше 0 и меньше {self.fieldSize}. Повторите ввод.")
				continue
			break

def printField(field):
	for str in field:
		print(str)

def whereToGo(field, iStr, iCol):
	steps = [[2,2, -2,-2, 1,1, -1,-1], [1,-1, 1,-1, 2,-2, 2,-2]]
	moves = [[], []]
	for i in range(len(steps[0])):
		niStr = iStr + steps[0][i]
		niCol = iCol + steps[1][i]
		if niStr >= 0 and niStr < len(field) and niCol >= 0 and niCol < len(field):
			if field[niStr][niCol] == 0:
				moves[0].append(niStr)
				moves[1].append(niCol)
	return moves

def game(field, iStr, iCol, count, maxCount):
	count += 1
	if count >= maxCount:
		return True
	moves = whereToGo(field,iStr,iCol)
	print(moves)
	if len(moves[0]) < 1:
		return False

	for i in range(len(moves[0])):
		buf = field.copy()
		buf[moves[0][i]][moves[1][i]] = count
		if game(buf, moves[0][i], moves[1][i], count, maxCount):
			field.clear()
			field.extend(buf)
			buf.clear()
			return True
		else:
			buf.clear()

def startGame():
	print("Запущенна игра Конь шахмотный")
	startValue = StartingValue()
	field = [[0 for i in range(startValue.fieldSize)] for j in range(startValue.fieldSize)]
	field[startValue.indStrHorse][startValue.indColumnHorse] = 1
	print(game(field, startValue.indStrHorse, startValue.indColumnHorse, 1, startValue.fieldSize ** 2))
	printField(field)