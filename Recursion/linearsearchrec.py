items = [3,9,2,10,4,6,5,7,8,1]

def linsearch(data,target,pointer):
  item = data[pointer]
  if item == target:
    return pointer
  elif len(data[pointer+1:]) == 0:
    return -1
  else:
    return linsearch(data,target,pointer + 1)
  #end if
#end function

print(linsearch(items, 19,0))


items = [3,9,2,10,4,6,5,7,8,1]

def bubble_sort_pass(array, ap, size):
    # We return the number of swaps in this iteration. 
    swaps = 0

    # If the array contains 0 or 1 elements, it is already sorted. 
    if (size < 2):
        return swaps
    #end if

    # Array contains at least 2 elements. 
    if (array[ap] > array[ap+1]):
        # First two elements are in wrong order. We need to swap them. 
        array[ap],array[ap+1] = array[ap+1],array[ap]
        swaps += 1
    #end if

    # Recursively bubble sort the array starting at the 2nd element. 
    swaps = swaps + bubble_sort_pass(array, ap+1, size - 1)
    return swaps
#end function

def bubble_sort(array, ap, size):
    # Do one pass of bubble sorting the entire array. 
    swaps = bubble_sort_pass(array, ap, size)

    # If there was at least one swap, we have to do another pass. 
    if (swaps >= 1):
        bubble_sort(array,ap, size)
    #end if
#end function


    
bubble_sort(items,0, 10)

print(items)


