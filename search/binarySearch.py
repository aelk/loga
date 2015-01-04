from bisect import bisect_left

def search(A, key, low = 0, high = None):
    if high is None:
        high = len(A)
    pos = bisect_left(A, key, low, high)
    if A[pos] == key:
    	return pos
    else:
    	return -1
