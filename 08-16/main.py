uStr = input("Введите строку: ")
arrWords = uStr.split()
maxLenWord = arrWords[0]
minLenWord = arrWords[0]

for i in range(1, len(arrWords)):
	if len(maxLenWord) < len(arrWords[i]):
		maxLenWord = arrWords[i]
	if len(minLenWord) > len(arrWords[i]):
		minLenWord = arrWords[i]

maxCountChar = [uStr[0], uStr.count(uStr[0])]
oldChar = maxCountChar[0]
for i in range(1, len(uStr)):
	if uStr[i] != ' ' and oldChar.find(uStr[i]) < 0:
		oldChar += uStr[i]
		if uStr.count(uStr[i]) > maxCountChar[1]:
			maxCountChar = [uStr[i], uStr.count(uStr[i])]


print(f"Самое длинное слово: {maxLenWord}\n"
	  f"Самое короткое слово: {minLenWord}\n"
	  f"Самый повторяющийся символ: \'{maxCountChar[0]}\' (повторяется {maxCountChar[1]} раз)")