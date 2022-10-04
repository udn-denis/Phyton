"""def decor(func):
	def wrap(*args, **kwargs):
		print("*************")
		func(*args, *kwargs)
		print("*************")
		return
	return wrap



def printFunc(t, tp= ""):
	tp = tp.upper()
	if 'Y' in tp:
		print("Сейчас {} год".format(t.tm_year))
	if 'MON' in tp:
		monList = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
		print("Месяц {}".format(monList[t.tm_mon-1]))
	if 'D' in tp:
		print("{} день".format(t.tm_mday))
	if 'H' in tp:
		print("{} час(ов)".format(t.tm_hour))
	if 'M' in tp:
		print("{} минут(а)".format(t.tm_min))
	if 'S' in tp:
		print("{} секунд(а)".format(t.tm_sec))

@decor
def firstFunc(func):
	def gettime(func):
		import time
		named_tuple = time.localtime()
		func(named_tuple, "y mon d h m s")
	gettime(func)

firstFunc(printFunc)
"""
def decPizza1(clPizza):
	def wrap():
		class Pizza(clPizza):
			def __init__(self):
				super().__init__()
				self.tomatoes = "4 ломтика ароматных помидор"
				self.cheese = "4 вкусных сыра"
		obj = Pizza
		return obj
	return wrap()



@decPizza1
class EmptyPizza:
	def __init__(self):
		self.basis = "Лепешка"
		self.sauce = "Секретный"



pizza1 = EmptyPizza()

print(pizza1.__dict__)