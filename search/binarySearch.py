from bisect import bisect_left

def search(A, key, low = 0, high = None):
    if len(A) == 0:
        return -1
    elif len(A) == 1:
        if A[0] == key:
            return 0
        else: 
            return -1
    if high is None:
        high = len(A)
    pos = bisect_left(A, key, low, high)
    if A[pos] == key:
    	return pos
    else:
    	return -1
