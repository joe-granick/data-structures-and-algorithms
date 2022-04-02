
def swap_list(a, b):
    return (b, a)

test = [1, 2, 3 , 4, 5]
print(test)
swapped= swap_list(test[0], test[1])
test[0] = swapped[0]
test[1] = swapped[1]
print(test)


def bubble_sort(unsorted_list, index = 0, list_sorted = True, last_index = 0, first_pass = True, steps = 0):
    if first_pass:
        last_index = len(unsorted_list)
    if index+1 < last_index:
        if unsorted_list[index] > unsorted_list[index+1]:
            swapped = swap_list(unsorted_list[index], unsorted_list[index+1])
            unsorted_list[index] = swapped[0]
            unsorted_list[index+1] = swapped[1]
            list_sorted = False
            steps+=1
        index+=1
        return bubble_sort(unsorted_list, index, list_sorted,last_index = last_index, first_pass = False, steps = steps+1)
    elif list_sorted:
        list_info = (unsorted_list, len(unsorted_list), steps)
        return list_info
    else:
        return bubble_sort(unsorted_list, index = 0, list_sorted = True, last_index = last_index-1, first_pass = False, steps = steps) 
    



bubble_sort_test = bubble_sort([4, 2, 7, 1, 3])
sorted_list, n, o = bubble_sort_test[0], bubble_sort_test[1], bubble_sort_test[2] 
print("n: {} bubble sort efficiency: {} O(n^2): {}   sorted list: {}".format(n, o, n*n, sorted_list))

bubble_sort_test = bubble_sort([5, 4, 3, 2, 1])
sorted_list, n, o = bubble_sort_test[0], bubble_sort_test[1], bubble_sort_test[2] 
print("n: {} bubble sort efficiency: {} O(n^2): {}   sorted list: {}".format(n, o, n*n, sorted_list))

bubble_sort_test = bubble_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
sorted_list, n, o = bubble_sort_test[0], bubble_sort_test[1], bubble_sort_test[2] 
print("n: {} bubble sort efficiency: {} O(n^2): {}   sorted list: {}".format(n, o, n*n, sorted_list))

bubble_sort_test = bubble_sort([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
sorted_list, n, o = bubble_sort_test[0], bubble_sort_test[1], bubble_sort_test[2] 
print("n: {} bubble sort efficiency: {} O(n^2): {}   sorted list: {}".format(n, o, n*n, sorted_list))
#complexity
#bubble sort has two tyoes of steps
#comparisons
#increment
        

