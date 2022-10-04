
def dayInYear(year):
	if year % 4 == 0:
		return 366
	else:
		return 365


def dayInMounth(mounth,year):
	if mounth == 2:
		if year % 4 == 0:
			return 29
		else:
			return 28
	else:
		if mounth < 8:
			if mounth % 2 == 0:
				return 30
			else:
				return 31
		else:
			if mounth % 2 != 0:
				return 30
			else:
				return 31

def difday (d1,m1,y1,d2,m2,y2):
	deltaDay = 0
	if y1 == y2:
		if m1 == m2:
			return d2 - d1
		else:
			deltaDay += dayInMounth(m1,y1) - d1
			for mounth in range(m1+1,m2):
				deltaDay += dayInMounth(mounth,y1)
			deltaDay += d2
			return deltaDay
	else:
		deltaDay += dayInMounth(m1,y1) - d1
		for mounth in range(m1 + 1, 12+1):
			deltaDay += dayInMounth(mounth,y1)
		for year in range(y1+1,y2):
			deltaDay += dayInYear(year)

		for mounth in range(1, m2):
			deltaDay += dayInMounth(mounth,y2)
		deltaDay += d2
		return deltaDay

print(difday(1,1,1995,1,1,1996))

