# https://www.geeksforgeeks.org/quick-sort/
# Small changes by Paul Lu

# Python program for implementation of Quicksort Sort 

# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
	pivotIndex = ( low-1 )		 # index of smaller element 
	pivotKey = arr[high]	 # pivot value

	for currIndex in range(low , high): 

		# If current element is smaller than or 
		# equal to pivot value
		if arr[currIndex] <= pivotKey: 
		
			# increment index of smaller element 
			pivotIndex = pivotIndex+1
			arr[pivotIndex],arr[currIndex] = arr[currIndex],arr[pivotIndex] 

	# Move pivot value to acutal final location
	arr[pivotIndex+1],arr[high] = arr[high],arr[pivotIndex+1] 
	return ( pivotIndex+1 ) 

# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low --> Starting index, 
# high --> Ending index 

# Function to do Quick sort 
def quickSort(arr,low,high): 
	if low < high: 

		# pi is partitioning index, arr[p] is now 
		# at right place 
		pivotIndex = partition(arr,low,high) 

		# Separately sort elements before 
		# partition and after partition 
		quickSort(arr, low, pivotIndex-1) 
		quickSort(arr, pivotIndex+1, high) 

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
	print ("%d " %arr[i], end=""), 
print()

# This code is contributed by Mohit Kumra 
