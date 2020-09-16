def fibonacci (n):
	"""Числа Фибоначчи"""
	l=1
	m=0
	F=1
	print (F) #выводит первое число
	sum=0
	for i in range(n):
		if F<n:
			F=l+m
			print (F) #выводит числа Фибоначчи
			if F%2==0:
				sum+=F #сумма чисел Фибоначчи
			m=l
			l=F
			i+=1
	print("Сумма равна {}".format(sum))