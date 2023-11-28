import time
import random

NumElement = 8192

class TimeObj():
    def __init__(self, msg=""):
        self._msg = msg
        self._start = time.perf_counter()
        self.tick()
        self.tock()

    def tick(self,print_clock=False):
        self._tick_save = time.perf_counter()

    def tock(self,print_clock=False):
        self._tock_save = time.perf_counter()
        if(print_clock):
            print(self._msg,self.__str__())

    def __str__(self):
        assert(self._tock_save > self._tick_save), "Non-monotonic"
        t = self._tock_save - self._tick_save
        assert(float(t)>0.0), "Non-monotonic 2"
        s = ("%f" % (t)) + "s"
        return(s)

def partition(arr,low,high):
    pivotIndex = ( low-1 )       # index of smaller element 
    pivotKey = arr[high]     # pivot value

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


def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements 
    for i in range(n):

        # Last i elements are already in place 
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Not the cleverest way to do this
def rand_list_ints(l,num):
    for i in range(num):
        l.append(random.randint(0,NumElement))


def test_main():
    a = TimeObj("All:")

    b = TimeObj("Create:")
    my_list = []
    rand_list_ints(my_list,NumElement)
    b.tock(True)

    c = TimeObj("Sort:")
    c.tick()
    my_list.sort()
    c.tock()

    print("Built-in Sorting:",c)

    a.tock(True)

    # User-defined quicksort
    a = TimeObj("All:")

    b = TimeObj("Create:")
    my_list = []
    rand_list_ints(my_list,NumElement)
    b.tock(True)

    c = TimeObj("QuickSort:")
    c.tick()
    quickSort(my_list,0,len(my_list)-1)
    c.tock()

    print("Quick Sorting:",c)

    a.tock(True)

    # User-defined bubblesort
    a = TimeObj("All:")

    b = TimeObj("Create:")
    my_list = []
    rand_list_ints(my_list,NumElement)
    b.tock(True)

    c = TimeObj("bubblesort:")
    c.tick()
    bubbleSort(my_list)
    c.tock()

    print("Bubble Sorting:",c)

    a.tock(True)

if __name__ == "__main__":
    test_main()
