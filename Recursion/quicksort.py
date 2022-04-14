def pivot(array, left_index = 0, pivot_index = None, right_index = None):
    print(array)
    if pivot_index is None:
        pivot_index = len(array)-1
    if right_index is None:
        right_index = pivot_index-1
    while array[left_index] < array[pivot_index] and left_index < pivot_index:
        left_index+=1
    while array[right_index] > array[pivot_index] and right_index > 0:
        right_index-=1
    if left_index >= right_index:
        print("swap left and pivot")
        array[pivot_index], array[left_index] = array[left_index], array[pivot_index]
        return [array, left_index]
    else:
        print("swap right and left")
        array[right_index], array[left_index] = array[left_index], array[right_index]
        return pivot(array, left_index, pivot_index, right_index)

def quicksort(array):
    print(array)
    if len(array) <= 2:
        #print(array)
        return array
    else:
        array_pivot = pivot(array)
        pivot_index = array_pivot[1]
        pivot_val = array_pivot[0][pivot_index]
        left_array = array_pivot[0][:pivot_index]
        right_array = array_pivot[0][pivot_index+1:]
        return quicksort(left_array) + [pivot_val] + quicksort(right_array)
    

print(pivot([5, 7, 6, 8, 3, 2, 1, 0]))
print(quicksort([5, 7, 6, 8, 3, 2, 1, 0]))
