def quicksort(array):
    def pivot(array):
        pivot = len(array)-1
        left_index = 0
        right_index = pivot - 1
        while array[left_index] < array[pivot] and left_index < len(array)-1:
            left_index+=1
        while array[right_index] > array[pivot] and right_index >0:
            right_index-=1
        if right_index == left_index:
            move_val = right_index
            pivot_val = array[pivot]
            array[right_index] = pivot_val
            array[pivot] = move_val
            pivot = right_index
            left_array = array[:pivot]
            right_array = array[pivot+1:]
            return[left_array, pivot, right_array]
    if len(array) == 1:
       return array[0]
    else:
        partitioned = pivot(array)
        left_array, pivot, right_array = partitioned[0], partitioned[1], partitioned[2]
        return quicksort(left_array) + pivot + quicksort(right_array)

    


print(quicksort([0, 1, 2, 3, 6, 5]))
