def sort(arr):
	"""Quicksort first requires a pivot to be used as a comparison.
	The array is then split into two parts. The elements of the first part
	are smaller than the pivot, and those of the second part are greater than it.
	Each part is recursively sorted, and joining them to the pivot is the sorted array."""
	if len(arr) <= 1:
		return arr
	else:
		pivot   = arr[0]
		smaller = [x for x in arr[1:] if x <= pivot]
		greater = [x for x in arr[1:] if x > pivot]
		# Now recursively sort the two parts:
		smaller = sort(smaller)
		greater = sort(greater)
		return smaller + [pivot] + greater
