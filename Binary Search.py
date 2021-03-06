'''Binary Search Algorithm
Binary search works on sorted arrays. Binary search begins by comparing an element in the middle of the array with the target value. 
If the target value matches the element, its position in the array is returned. 
If the target value is less than the element, the search continues in the lower half of the array. 
If the target value is greater than the element, the search continues in the upper half of the array. 
By doing this, the algorithm eliminates the half in which the target value cannot lie in each iteration
Big O Time  = O(logN)
From WikiPedia'''

def binarySearch(array, value, low, high):
	if low > high:
		return False
	mid = (low+high) / 2
	if array[mid] > value:
		return binarySearch(array, value, low, mid-1)
	elif array[mid] < value:
		return binarySearch(array, value, mid+1, high)
	else:
		return mid
