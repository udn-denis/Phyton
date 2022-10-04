import module1, module2,inspect
def fmax(*args):
	return max(args)

def sumRange(a,b, *,c=0,d=0):
	sum = 0
	while a < b:
		sum += a
		a += 0.1
	return sum

def isPrimeNumber(num):
	if num < 1:
		return False
	for i in range(2, num):
		if num % i == 0:
			return False
	return True


def finsp(func):
	print("Название функции:", func.__name__)
	fargs = inspect.getfullargspec(func)
	print("Cписок имен позиционных параметров:", fargs.args)
	print("Имя параметра *:", fargs.varargs)
	print("Имя параметра **:", fargs.varkw)
	print("Аргументы с значением по умолчанию:", fargs.kwonlyargs)

def isLuckyNum (num):
	if num < 100000 or num > 999999:
		print("Число не шестизначное!")
	sumA = 0
	sumB = 0
	for i in range(6):
		if i < 3:
			sumB += int(num % 10)
		else:
			sumA += int(num % 10)
		num = int(num / 10)
	return sumA == sumB
import string
def charC (chOld, key):
	i = string.ascii_uppercase.index(chOld)
	i += key
	if i >= len(string.ascii_uppercase):
		i -= len(string.ascii_uppercase)

	return string.ascii_uppercase[i]
def caesarCipher(str, key = 1, isDecoder = False):
	if isDecoder:
		key = -key

	newStr = ""
	str = str.upper()
	for i in range(len(str)):
		newStr += charC(str[i], key)
	return newStr



print(fmax(1,2,3,4,5,6))
print(sumRange(0.1, 1.0))
print(isPrimeNumber(8))
print(isLuckyNum(666666))

newStr = caesarCipher("abcdz", 2)
print(newStr)
print(caesarCipher(newStr, 2, True))

# finsp(sumRange)
# finsp(fmax)