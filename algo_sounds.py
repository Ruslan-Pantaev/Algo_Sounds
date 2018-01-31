import os
# import click

# @click.command()

duration = 0.001  # second
freqs = [110, 220, 440, 660]  # Hz
freq = 440  # Hz
pitch_multiplier = 180
# to use the following, brew install sox
# for x in range(0,4):
# 	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freqs[x]))

# ---------------------------------------------------------------------------------------------------------------------- 

def bubbleSort(arr):
    os.system('say "bubble sort initialized and commencing"')
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
                os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, (j*pitch_multiplier)))
    os.system('say "bubble sort complete!"')
 
# arr = [64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90,
# 	64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90]

# bubbleSort(arr)

# print ("Sorted array is:")
# for i in range(len(arr)):
#     print ("%d" %arr[i]),

# ----------------------------------------------------------------------------------------------------------------------

def recursiveBubbleSort(listt):
    for i, num in enumerate(listt):
        try:
            if listt[i+1] < num:
                listt[i] = listt[i+1]
                listt[i+1] = num
                os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, (i*pitch_multiplier)))
                recursiveBubbleSort(listt)
        except IndexError:
            pass    
    return listt

# Code contributed by Mohit Gupta_OMG

# listt = [64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90,
# 	64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90]

# putting the say cmds outside of function, otherwise they get called recursively...

# os.system('say "recursive bubble sort initialized and commencing"')
# recursiveBubbleSort(listt)
# os.system('say "recursive bubble sort complete!"')

# ----------------------------------------------------------------------------------------------------------------------

def selectionSort(arr):
	# Traverse through all array elements
	os.system('say "selection sort initialized and commencing"')
	for i in range(len(arr)):
	     
	    # Find the minimum element in remaining 
	    # unsorted array
	    min_idx = i
	    for j in range(i+1, len(arr)):
	        if arr[min_idx] > arr[j]:
	            min_idx = j
	            os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, (j*pitch_multiplier)))
	             
	    # Swap the found minimum element with 
	    # the first element        
	    arr[i], arr[min_idx] = arr[min_idx], arr[i]
	os.system('say "selection sort complete!"')

# arr = [64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90,
# 	64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90]

# selectionSort(arr)

# Driver code to test above
# print ("Sorted array")
# for i in range(len(A)):
#     print("%d" %A[i]),

# ----------------------------------------------------------------------------------------------------------------------

def insertionSort(arr):
    os.system('say "insertion sort initialized and commencing"')
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
                if j >= 1:
                	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, (j*pitch_multiplier)))
        arr[j+1] = key
    os.system('say "insertion sort complete!"')

# This code is contributed by Mohit Kumra
 
# arr = [64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90,
# 	64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90]

# insertionSort(arr)

# print ("Sorted array is:")
# for i in range(len(arr)):
#     print ("%d" %arr[i])

# ----------------------------------------------------------------------------------------------------------------------

def recursiveInsertionSort(arr,n):
    # base case
    if n<=1:
        return
     
    # Sort first n-1 elements
    recursiveInsertionSort(arr,n-1)
    '''Insert last element at its correct position
        in sorted array.'''
    last = arr[n-1]
    j = n-2
     
      # Move elements of arr[0..i-1], that are
      # greater than key, to one position ahead
      # of their current position 
    while (j>=0 and arr[j]>last):
        arr[j+1] = arr[j]
        j = j-1
        if j >= 1:
        	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, (j*pitch_multiplier)))
    arr[j+1]=last
     
# A utility function to print an array of size n
def printArray(arr,n):
    for i in range(n):
        print (arr[i]),

# Contributed by Harsh Valecha

# arr = [64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90,
# 	64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90]
# n = len(arr)

# os.system('say "recursive insertion sort initialized and commencing"')
# recursiveInsertionSort(arr, n)
# os.system('say "recursive insertion sort complete!"')

# printArray(arr, n)

# ----------------------------------------------------------------------------------------------------------------------

# recursive
def mergeSort(alist):
    # print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
            os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, (k*pitch_multiplier)))

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
            os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, (i*pitch_multiplier)))

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
            os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, (j*pitch_multiplier)))
    # print("Merging ",alist)
 
# arr = [64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90,
# 	64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90]

# os.system('say "merge sort initialized and commencing"')
# mergeSort(arr)
# os.system('say "merge sort complete!"')

# ----------------------------------------------------------------------------------------------------------------------

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low , high):
 
        # If current element is smaller than or
        # equal to pivot
        if   arr[j] <= pivot:
         
            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
            os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, (j*pitch_multiplier)))
 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, (i*pitch_multiplier)))
    return ( i+1 )
 
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
def quickSort(arr,low,high):
    if low < high:
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, (low*pitch_multiplier)))
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
 
# Driver code to test above
# arr = [64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90,
# 	64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90]
# n = len(arr)

# os.system('say "quick sort initialized and commencing"')
# quickSort(arr,0,n-1)
# os.system('say "quick sort complete!"')

# print ("Sorted array is:")
# for i in range(n):
    # print ("%d" %arr[i]),
 
# This code is contributed by Mohit Kumra

# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------

# FUNCTION CALLS
# ----------------------------------------------------------------------------------------------------------------------

arr = [64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90,
	64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

# ----------------------------------------------------------------------------------------------------------------------

listt = [64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90,
	64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90]

os.system('say "recursive bubble sort initialized and commencing"')
recursiveBubbleSort(listt)
os.system('say "recursive bubble sort complete!"')

# ----------------------------------------------------------------------------------------------------------------------

arr = [64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90,
	64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90]

selectionSort(arr)

# ----------------------------------------------------------------------------------------------------------------------

arr = [64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90,
	64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90]

insertionSort(arr)

# ----------------------------------------------------------------------------------------------------------------------

arr = [64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90,
	64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90]
n = len(arr)

os.system('say "recursive insertion sort initialized and commencing"')
recursiveInsertionSort(arr, n)
os.system('say "recursive insertion sort complete!"')

# ----------------------------------------------------------------------------------------------------------------------

arr = [64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90,
	64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90]

os.system('say "merge sort initialized and commencing"')
mergeSort(arr)
os.system('say "merge sort complete!"')

# ----------------------------------------------------------------------------------------------------------------------

arr = [64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90,
	64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90, 64, 34, 25, 12, 22, 11, 90]
n = len(arr)

os.system('say "quick sort initialized and commencing"')
quickSort(arr,0,n-1)
os.system('say "quick sort complete!"')

# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------























