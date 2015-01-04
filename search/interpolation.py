def search(A, key, low = 0, high = None):
	if len(A) == 0:
		return -1
	elif len(A) == 1:
		return 0 if (A[0] == key) else -1

	if high is None:
		high = len(A) - 1

	while (A[low] <= key) and (A[high] >= key):
		mid = low + ((key - A[low]) * (high - low)) // (A[high] - A[low])
		if A[mid] < key:
			low = mid + 1
		elif A[mid] > key:
			high = mid - 1
		else:
			return mid

	return low if (A[low] == key) else -1
