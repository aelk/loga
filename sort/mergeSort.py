import heapq

def mergeSort(arr):
	"""Merge sort splits the input into two arrays,
	recursively sorts each array, and then combines the two
	with a merge subroutine (in this case from heapq)."""
	if len(arr) <= 1:
		return arr

	mid = len(arr) // 2
	left = arr[:mid]
	right = arr[mid:]

	left = mergeSort(left)
	right = mergeSort(right)
	return list(heapq.merge(left, right))
