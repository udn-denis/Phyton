# try:
# 	file = open("file.txt", "wt", encoding= "utf-8")
#
#
# 	file.writelines([str(i)+"\n" for i in range(5)])
# 	file.close()
# except Exception as exp:
# 	print("Что то пошло не так:(\n", exp)

import string
#
# try:
# 	file1, file2 = open("file.txt", "rt", encoding="utf-8"),open("newfile.txt", "wt", encoding="utf-8")
#
# 	bufer = file1.read()
#
# 	listWords = bufer.split()
# 	newWords = ""
# 	for i in range(len(listWords)):
# 		listWords[i] = listWords[i].strip(string.punctuation)
# 		if len(listWords[i]) == 7:
# 			newWords += listWords[i] + "\n"
#
#
# 	file2.write(newWords)
# 	file1.close()
# 	file2.close()
# except Exception as exp:
# 	print("Что то пошло не так:(\n", exp)

#-------------------------------------------------------------------------------
try:
	with open("file.txt", "wt", encoding= "utf-8") as fr:
		with open("file.txt", "wt", encoding="utf-8") as fw:
			listLines = fr.readlines()
			for line in listLines:



except Exception as exp:
	print("Что то пошло не так:(\n", exp)