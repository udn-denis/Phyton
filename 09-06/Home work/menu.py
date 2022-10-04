def __printMenu(questionFileName):
	f = open(questionFileName,"rt", encoding = "utf-8")
	print(f.read())
	f.close()

def menu(questionFileName, *tasks):
	__printMenu(questionFileName)
	tasksCount = len(tasks)
	while True:
		print(f"{tasksCount+1}. Для повторного вывода меню.")
		try:
			numTask = int(input("Введите номер задания: "))
		except:
			print("Не корректное значение!!!\n"
				  "Попробуйте ввести ещё раз.")
			continue
		if numTask < 0 or numTask > tasksCount+1:
			print(f"Значение может быть от 0 до {tasksCount+1}\n"
				  f"Попробуйте ввести ещё раз.")
			continue

		if numTask == 0:
			return True
		elif numTask == tasksCount+1:
			__printMenu(questionFileName)
		else:
			tasks[numTask-1]()