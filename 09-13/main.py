from string import punctuation
def censorship():
	inText = ""
	censorshipWords = ""
	with open("user_text.txt", "rt", encoding="utf-8") as f1:
		inText = f1.read()
	with open("censorship.txt", "rt", encoding="utf-8") as f2:
		censorshipWords = f2.read()
	censorshipWords = censorshipWords.split("\n")
	inText = inText.split(" ")
	for censor in censorshipWords:
		for i in range(len(inText)):
			if censor in inText[i]:
				strBuf=""
				for j in range(len(inText[i])):
					if inText[i][j] in punctuation:
						strBuf += inText[i][j:]
						break
					else:
						strBuf += '*'
				inText[i] = strBuf
	inText = " ".join(inText)
	with open("new_user_text.txt", "wt", encoding= "utf-8") as f3:
		f3.write(inText)


def translit():
	vocabulary = []
	with open("vocabulary.txt", "rt", encoding="utf-8") as f1:
		vocabulary.append(f1.readline().strip("\n"))
		vocabulary.append(f1.readline())
	with open("user_text.txt", "rt", encoding="utf-8") as f2:
		usertext = f2.read()
	vocabulary[0] = vocabulary[0].split(" ")
	vocabulary[1] = vocabulary[1].split(" ")
	usertext = usertext.lower()
	newText = ""
	for i in range(len(usertext)):
		try:
			newText += vocabulary[1][vocabulary[0].index(usertext[i])]
		except ValueError:
			newText += usertext[i]
	with open("new_user_text.txt", "wt", encoding="utf-8") as f3:
		f3.write(newText)


def mergingFile ():
	print("Вводите имена файлов. Для выхода введите 'quit'")
	count = 1
	fileNames = []
	while True:
		fileName = input(f"{count} файл: ")
		if fileName == "quit":
			break
		else:
			fileNames.append(fileName)
		count += 1
	# for fileName in fileNames



if __name__ == "__main__":
	translit()