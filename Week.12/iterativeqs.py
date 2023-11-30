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

# https://www.geeksforgeeks.org/iterative-quick-sort/

# Function to do Quick sort 
# arr[] --> Array to be sorted, 
# l  --> Starting index, 
# h  --> Ending index 
def quickSortIterative(arr, l, h): 
  
    # Create an auxiliary stack 
    size = h - l + 1
    stack = [0] * (size) 
  
    # initialize top of stack 
    top = -1
  
    # push initial values of l and h to stack 
    top = top + 1
    stack[top] = l 
    top = top + 1
    stack[top] = h 
  
    # Keep popping from stack while is not empty 
    while top >= 0: 
  
        # Pop h and l 
        h = stack[top] 
        top = top - 1
        l = stack[top] 
        top = top - 1
  
        # Set pivot element at its correct position in 
        # sorted array 
        p = partition( arr, l, h ) 
  
        # If there are elements on left side of pivot, 
        # then push left side to stack 
        if p-1 > l: 
            top = top + 1
            stack[top] = l 
            top = top + 1
            stack[top] = p - 1
  
        # If there are elements on right side of pivot, 
        # then push right side to stack 
        if p + 1 < h: 
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h 

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("I-Sorted array is:") 
for i in range(n): 
	print ("%d " %arr[i], end=""), 
print()

# This code is contributed by Mohit Kumra 
