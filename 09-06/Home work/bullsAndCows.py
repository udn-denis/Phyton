from random import randint

def printResult(bullsCount, cowsCount):
	if bullsCount == 0:
		endingBulls = 'ов'
	elif bullsCount == 1:
		endingBulls = ''
	else:
		endingBulls= 'а'

	if cowsCount == 0:
		endingCows = ''
	elif bullsCount == 1:
		endingCows = 'а'
	else:
		endingCows= 'ы'

	print(f"{bullsCount} бык{endingBulls};\n"
		  f"{cowsCount} коров{endingCows}.")

def game(rndNum):
	while True:
		try:
			uNum = int(input("Введите ваше число: "))
		except:
			print("Вы ввели не корректное значение. Попробуйте ещё раз.")
			continue
		if uNum < 1000 or uNum > 9999:
			print("Число должно быть 4-х значным. Повторите ввод.")
			continue
		break
	if uNum == rndNum:
		print("Вы угадали число!!! Поздравляю!)")
		return 1
	uNumStr = str(uNum)
	rndNumStr = str(rndNum)
	bullsCount = 0
	cowsCount = 0

	for i in range(len(rndNumStr)):
		if uNumStr[i] in rndNumStr:
			bullsCount += 1
		if uNumStr[i] == rndNumStr[i]:
			cowsCount += 1

	printResult(bullsCount, cowsCount)
	return game(rndNum) + 1

def startGame():
	print("Запущенна игра Быки и коровы")
	rndNum = randint(1000, 9999)
	print ("Бот загадал 4-х значное число. Попробуйте его угадать.")
	count = game(rndNum)

	if count == 1:
		endingCount = 'ку'
	elif count > 1 and count < 5:
		endingCount = 'ки'
	else:
		endingCount= 'ок'

	print(f"У вас получилось угадать число за {count} попыт{endingCount}")