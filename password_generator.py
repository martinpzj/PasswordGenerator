import random

#combination of numbers, symbols, uppercase letters, lowercase letters

def generator(length):
	password = ''
	while len(password) != length:
		password = password + random.choice(characters)
	return password


characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'

while True:
	#Ask user how long they want their password to be
	print('Password ranges from 8-16 characters long')
	password_length = int(input('Type password length: '))

	if password_length >= 8 and password_length <= 16:
		if password_length == 8:
			for num in range(10):
				new = generator(password_length)
				print(new)
			break
		elif password_length == 9:
			for num in range(10):
				new = generator(password_length)
				print(new)
			break
		elif password_length == 10:
			for num in range(10):
				new = generator(password_length)
				print(new)
			break
		elif password_length == 11:
			for num in range(10):
				new = generator(password_length)
				print(new)
			break
		elif password_length == 12:
			for num in range(10):
				new = generator(password_length)
				print(new)
			break
		elif password_length == 13:
			for num in range(10):
				new = generator(password_length)
				print(new)
			break
		elif password_length == 14:
			for num in range(10):
				new = generator(password_length)
				print(new)
			break
		elif password_length == 15:
			for num in range(10):
				new = generator(password_length)
				print(new)
			break
		elif password_length == 16:
			for num in range(10):
				new = generator(password_length)
				print(new)
			break
		else: break

	#Password was too long
	elif password_length > 8:
		print('Password length was too long')
		continue
	#Password was too short
	else:
		print('Password length was too short')
		continue