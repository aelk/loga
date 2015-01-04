def listPrimes(n):
	'''Returns a list of primes below n.'''
	numbers = set(range(n, 1, -1))
	primes = []

	while numbers:
		p = numbers.pop()
		primes.append(p)
		# Remove each multiple of p from numbers:
		numbers.difference_update(set(range(p * 2, n + 1, p)))
	return primes
