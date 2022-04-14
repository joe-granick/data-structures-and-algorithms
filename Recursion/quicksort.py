def pivot(array, left_index = 0, pivot_index = None, right_index = None):
    #print(array)
    if pivot_index is None:
        pivot_index = len(array)-1
    if right_index is None:
        right_index = pivot_index-1
    while array[left_index] < array[pivot_index] and left_index < pivot_index:
        left_index+=1
    while array[right_index] > array[pivot_index] and right_index > 0:
        right_index-=1
    if left_index >= right_index:
        #print("swap left and pivot")
        array[pivot_index], array[left_index] = array[left_index], array[pivot_index]
        return [array, left_index]
    else:
        #print("swap right and left")
        array[right_index], array[left_index] = array[left_index], array[right_index]
        print(array)
        return pivot(array, left_index, pivot_index, right_index)

def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        array_pivot = pivot(array)
        pivot_index = array_pivot[1]
        pivot_val = array_pivot[0][pivot_index]
        left_array = array_pivot[0][:pivot_index]
        right_array = array[pivot_index+1:]
        return quicksort(left_array) + [pivot_val] + quicksort(right_array)
    
  
    




    
#if array[right_index] 
    # if len(array) == 1:
    #    return array[0]
    # else:
    #     partitioned = pivot(array)
    #     left_array, pivot, right_array = partitioned[0], partitioned[1], partitioned[2]
    #     return quicksort(left_array) + pivot + quicksort(right_array)

    
print(pivot([0, 5, 2, 1, 6, 3]))

print(quicksort([0, 5, 2, 1, 6, 3]))
#print(quicksort([0, 1, 2, 3, 6, 5]))
