from fractions import gcd

def lcm(a, b):
	"""Returns the least common multiple of a and b: that is, the
	smallest positive integer x such that a divides x and b divides x."""
	try:
		if a < 0:
			a *= -1
		return (a / gcd(a,b)) * b
	except ZeroDivisionError:
		print("Error: the least common multiple of two zeros is undefined.")
		return None
