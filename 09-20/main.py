# Full name
# Date of Birth
# telephone
# City, country
# address
class Human:
    def __init__(self, fullName = "", dateOfBirth = "", tel = "", city = "", country = "", address = ""):
        self.__fullName__ = fullName
        self.__dateOfBirth__ = dateOfBirth
        self.__tel__ = tel
        self.__city__ = city
        self.__country__ = country
        self.__address__ = address

    def setFullName(self, fullName):
        self.__fullName__ = fullName
    def setDateOfBirth(self, dateOfBirth):
        self.__dateOfBirth__ = dateOfBirth
    def setTel(self, tel):
        self.__tel__ = c
    def setCity(self, city):
        self.__city__ = city
    def setCountry(self, country):
        self.__country__ = country
    def setAddres(self, address):
        self.__address__ = address

    def getFullName(self):
        print(self.__fullName__)
    def getDateOfBirth(self):
        print(self.__dateOfBirth__)
    def getTel(self):
        print(self.__tel__)
    def getCity(self):
        print(self.__city__)
    def getCountry(self):
        print(self.__country__)
    def getAddres(self):
        print(self.__address__)

# Fraction
# numerator
# denominator

class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        self.__numerator__ = numerator
        self.__denominator__ = denominator

    def setNumerator (self, numerator):
        self.__numerator__ = numerator
    def setDenominator(self, denominator):
        self.__denominator__ = denominator

    def getNumerator(self):
        return  self.__numerator__
    def getDenominator(self):
        return  self.__denominator__

    def cut(self):
        while True:
            if self.__numerator__ < self.__denominator__:
                min = self.__numerator__
            else:
                min = self.__denominator__
            isCut = False
            for d in range(2, min):
                if self.__numerator__ % d == 0 and self.__denominator__ % d == 0:
                    self.__numerator__ //= d
                    self.__denominator__ //= d
                    isCut = True
                    break
            if not isCut:
                break





    # addition
    # subtraction
    # multiplication
    # division

    def add(self, fract):
        self.__numerator__ = self.getNumerator() * fract.getDenominator()  + self.getDenominator() * fract.getNumerator()
        self.__denominator__ = self.getDenominator() * fract.getDenominator()
        self.cut()

    def subtraction(self, fract):
        self.__numerator__ = self.getNumerator() * fract.getDenominator()  - self.getDenominator() * fract.getNumerator()
        self.__denominator__ = self.getDenominator() * fract.getDenominator()
        self.cut()

    def multiplication(self, fract):
        self.__numerator__ = self.getNumerator() * fract.getNumerator()
        self.__denominator__ = self.getDenominator() * fract.getDenominator()
        self.cut()

    def division(self, fract):
        self.__numerator__ = self.getNumerator() * fract.getDenominator()
        self.__denominator__ = self.getDenominator() * fract.getNumerator()
        self.cut()

a = Fraction(1,2)
b = Fraction(1,4)
a.add(b)
print(a.__dict__)