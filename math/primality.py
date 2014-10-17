import math

def check(n):
	'''Returns true if n is prime and false otherwise'''
	if n <= 3:
		return n >= 2
	if n % 2 == 0:
		return False
	for i in range(5, int(math.sqrt(n)) + 1, 2):
		if n % i == 0:
			return False
	return True
