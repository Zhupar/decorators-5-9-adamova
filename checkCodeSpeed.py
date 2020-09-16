import time
from fibonacci import fibonacci

class Check_code_speed:
	def __init__(self, num_runs):
		self.num_runs=num_runs
		self.start = 0
		self.end = 0
		self.num_runs=num_runs

	def __enter__(self):
		self.start = time.time()
		return self

	def __exit__(self, *args, **kwargs):
		self.end = time.time()
		print ("Код выплнен за {}".format(self.end-self.start))


	def __call__(self, func, *args, **kwargs):
		
		def func_wrapper(param):
			avg_time=0
			for i in range(self.num_runs):
				t0 = time.time()
				func(param)
				t1 = time.time()
				avg_time += (t1 - t0)
			avg_time /= param
			print (f"Выполнение заняло {avg_time} секунд")
		return func_wrapper		
	
if __name__ == '__main__':
	with Check_code_speed(3) as dec:
		fibonacci(4000000)	

