import re
import string

while True:
	username = input("Введите E-mail: ")
	if not re.fullmatch(r"[a-z0-9-_]+@[a-z-]+[.a-z]+", username):
		print("E-mail введён не корректно")
		continue
	break
print("E-mail - ГУД!!!")




while True:
	password = input("Введите пароль: ")
	if len(password) < 8:
		print("Длина пароля должна быть больше 8 символов!")

	if not re.search(r"["+string.punctuation+r"a-zA-Z0-9]+", password):
		print(f"Пароль должен состоять из заглавных и строчных символов латинского алфавита, цифр и символов: {string.punctuation}")
		continue

	if not re.search(r"[a-z]+", password):
		print("В пароле должен быть хотя бы один строчный символ латинского алфавита.")
		continue

	if not re.search(r"[A-Z]+", password):
		print("В пароле должен быть хотя бы один заглавный символ латинского алфавита.")
		continue

	if not re.search(r"\d+", password):
		print("В пароле должен быть хотя бы одна цифра.")
		continue

	if not re.search(r"\W+", password):
		print("В пароле должен быть хотя бы специальный символ.")
		continue
	break
print("Пароль - ГУД!!!")