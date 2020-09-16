import time

def timing(num_runs):
	def decorator(func):
		def func_wrapper(param):
			avg_time=0
			for i in range(num_runs):
				t0 = time.time()
				func(param)
				t1 = time.time()
				avg_time += (t1 - t0)
			avg_time /= param
			print (f"Выполнение заняло {avg_time} секунд")
		return func_wrapper
	return decorator



if __name__ == '__main__':
	@timing(3)
	def fibonacci (n):
		"""Числа Фибоначчи"""
		l=1
		m=0
		F=1
		# print (F) #выводит первое число
		sum=0
		for i in range(n):
			if F<n:
				F=l+m
				# print (F) #выводит числа Фибоначчи
				if F%2==0:
					sum+=F #сумма чисел Фибоначчи
				m=l
				l=F
				i+=1
		print("Сумма равна {}".format(sum))

	fibonacci(4000000)