def quicksort(array):
    pass
def pivot(array, left_index = 0, pivot_index = None, right_index = None):
    if pivot_index is None:
        pivot_index = len(array)-1
    if right_index is None:
        right_index = pivot_index-1

    if left_index == right_index:
        array[right_index], array[pivot_index] = array[pivot_index], array[right_index]#swap pivot and right inde
        return array
    elif array[left_index] <= array[pivot_index]:
        return pivot(array, left_index+1, pivot_index, right_index)
    elif array[right_index] < array[pivot_index]:
        array[right_index], array[pivot_index] = array[pivot_index], array[right_index]
        return pivot(array, left_index+1, pivot_index, right_index-1)
    else:
        return pivot(array, left_index, pivot_index, right_index-1)




    

    # if len(array) == 1:
    #    return array[0]
    # else:
    #     partitioned = pivot(array)
    #     left_array, pivot, right_array = partitioned[0], partitioned[1], partitioned[2]
    #     return quicksort(left_array) + pivot + quicksort(right_array)

    
print(pivot([0, 1, 2, 3, 6, 5]))

#print(quicksort([0, 1, 2, 3, 6, 5]))
