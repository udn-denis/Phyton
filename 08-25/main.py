import string
def printBoard(board):
	for boardString in board:
		for column in boardString:
			print(column, '  ', end= '')
		print(' ')
	print('  ')
#
# box = '*'
# board = [[box for i in range(9)] for j in range(9)]
#
#
# for i in range(1,9):
# 	board[0][i] = string.ascii_uppercase[i]
# for i in range(1,9):
# 	board[i][0] = str(i)
#
# line1= "RNBQKBNR"
# i=1
# for figure in line1:
# 	board[1][i] = figure
# 	board[-1][i] = figure
# 	i+=1
# for i in range(1,9):
# 	board[1][i] = 'P'
# 	board[-2][i] = 'P'
# 	i+=1
#
# printBoard(board)
#
# numStr = int(input("Введите кол-во строк: "))
# numColumn = int(input("Введите кол-во столбцов: "))
# uBoard = [[box for i in range(numColumn)] for j in range(numStr)]
#
# for i in range(numStr):
# 	for j in range(numColumn):
# 		uBoard[i][j] = input(f"Введите значения для {i} строки {j} столбца: ")
# printBoard(uBoard)
import random
def printArrayTemp(arr):
	for month in arr:
		printBoard(month)
		print("------\\\\\\\\\\------")
#
# yearTemperature = [[[0 for i in range(24)] for j in range(30)] for k in range(12)]
# for month in range(12):
# 	for day in range(30):
# 		for hour in range(24):
# 			yearTemperature[month][day][hour] = round(random.uniform(10, 30), 2)
# printArrayTemp(yearTemperature)
#
# averageArr = []
# for month in yearTemperature:
# 	for day in month:
# 		average = 0
# 		for hour in day:
# 			average += hour
# 		average /= len(day)
# 		averageArr.append(round(average,2))
# print(averageArr)
#
# countDayTemp20 = 0
# for average in averageArr:
# 	if average > 20:
# 		countDayTemp20 += 1
# print(f"Средняя температура за день была больше 20 градусов {countDayTemp20} дней")

# 3 дома 15 этажей 20 номеров

# homesCount = 3
# floorsCount = 15
# roomsCount = 20
#
# hotelArr = [[[random.choice([True, False]) for i in range(roomsCount)] for j in range(floorsCount)] for k in range(homesCount)]
# print(hotelArr)
# for homeNum in range(len(hotelArr)):
# 	print("Номер дома: ", homeNum + 1)
# 	for floorNum in range(len(hotelArr[homeNum])):
# 		print(f"Этаж {floorNum}:")
# 		for roomNum in range(len(hotelArr[homeNum][floorNum])):
# 			print(f"Номер {roomNum}: {hotelArr[homeNum][floorNum][roomNum]}; ", end= '')
# 	print("-------\\\\\\\-------")
count = 0
def sort (arr, a = 0):
	global count
	count += 1
	if a < len(arr) - 1 and a >= 0:
		if arr[a] < arr[a+1]:
			arr[a], arr[a+1] = arr[a+1], arr[a]
			sort(arr, a - 1)
		sort(arr, a+1)

countBlin = int(input("Введите кол-во блинов: "))

blinArr = [round(random.uniform(10,25), 1) for i in range(countBlin)]
print(blinArr)
sort(blinArr)
print(blinArr)
print(count)