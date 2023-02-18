#settings
import random
from random import *
score = 0

#Copyright
print('©Youngaymer 2023')
print('Score game v.1.0')


#Game
while True:
	print('Выберите режим:')
	print('* - умножение')
	print('+ - сложение')
	print('9 - счёт')
	print('0 - выход')
	v = str(input('Введите */+/9/0 : '))


	#Сложение
	if v == '+':

		while True:
			#Choice of complexity
			print('Выберите сложность:')
			print('1 - от 1 до 10')
			print('2 - от 1 до 20')
			print('3 - от 1 до 100')
			print('9 - счёт')
			print('0 - выход')
			v = int(input('Введите 1/2/3/9/0 : '))


			#Menu
			if v == 0:
				continue

			elif v == 1:

				while True:

					#Сложность 1
					z1 = randint(1,10)
					z2 = randint(1,10)
					print('Сколько будет ', z1, ' + ', z2, '?' )
					otvet = z1 + z2
					v = int(input('Введите ответ:'))
					if v == otvet:
						print('Правильно! +1 балл')
						score += 1
					elif v == 0:
						continue
					elif v == 9:
						print("Ваш счёт: ", score)
					else:
						print('Неправильно!')


			elif v == 2:

				while True:

					#Сложность 2
					z1 = randint(1,20)
					z2 = randint(1,20)
					print('Сколько будет ', z1, ' + ', z2, '?' )
					otvet = z1 + z2
					v = int(input('Введите ответ:'))
					if v == otvet:
						print('Правильно! +2 балла')
						score += 2
					elif v == 0:
						continue
					elif v == 9:
						print("Ваш счёт: ", score)
					else:
						print('Неправильно!')

			elif v == 3:

				while True:

					#Сложность 3
					z1 = randint(1,30)
					z2 = randint(1,30)
					print('Сколько будет ', z1, ' + ', z2, '?' )
					otvet = z1 + z2
					v = int(input('Введите ответ:'))
					if v == otvet:
						print('Правильно! +3 балла')
						score += 3
					elif v == 0:
						continue
					elif v == 9:
						print("Ваш счёт: ", score)
					else:
						print('Неправильно!')

			elif v == 9:
				print("Ваш счёт: ", score)
			else:
				print('Неправильно выбрана сложность')
				break

	elif v == '*':
		while True:
			#Choice of complexity
			print('Выберите сложность:')
			print('1 - от 1 до 10')
			print('2 - от 1 до 20')
			print('3 - от 1 до 100')
			print('9 - счёт')
			print('0 - выход')
			v = int(input('Введите 1/2/3/9/0 : '))


			#Menu
			if v == 0:
				continue

			elif v == 1:

				while True:

					#Сложность 1
					z1 = randint(1,10)
					z2 = randint(1,10)
					print('Сколько будет ', z1, ' * ', z2, '?' )
					otvet = z1 * z2
					v = int(input('Введите ответ:'))
					if v == otvet:
						print('Правильно! +2 балла')
						score += 2
					elif v == 0:
						continue
					elif v == 9:
						print("Ваш счёт: ", score)
					else:
						print('Неправильно!')


			elif v == 2:

				while True:

					#Сложность 2
					z1 = randint(1,20)
					z2 = randint(1,20)
					print('Сколько будет ', z1, ' * ', z2, '?' )
					otvet = z1 * z2
					v = int(input('Введите ответ:'))
					if v == otvet:
						print('Правильно! +4 балла')
						score += 4
					elif v == 0:
						continue
					elif v == 9:
						print("Ваш счёт: ", score)
					else:
						print('Неправильно!')

			elif v == 3:

				while True:

					#Сложность 3
					z1 = randint(1,30)
					z2 = randint(1,30)
					print('Сколько будет ', z1, ' * ', z2, '?' )
					otvet = z1 * z2
					v = int(input('Введите ответ:'))
					if v == otvet:
						print('Правильно! +6 баллов')
						score += 6
					elif v == 0:
						continue
					elif v == 9:
						print("Ваш счёт: ", score)
					else:
						print('Неправильно!')

			elif v == 9:
				print("Ваш счёт: ", score)
			else:
				print('Неправильно выбрана сложность')
				break


	elif v == '9':
		print("Ваш счёт: ", score)

	elif v == '0':
		continue

	else:
		print('Неправильно выбран режим!')