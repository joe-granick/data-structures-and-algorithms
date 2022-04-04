from tracemalloc import start


def swap_list(a, b):
    return (b, a)

def selection_sort(unsorted_list, start_index = 0, next_index =1, min_index = 0, steps = 0):
    if start_index == len(unsorted_list)-1:
        return (unsorted_list, start_index, len(unsorted_list), next_index, min_index, steps)
    elif next_index == len(unsorted_list):
        swapped_vals = swap_list(unsorted_list[start_index], unsorted_list[min_index])
        unsorted_list[start_index] = swapped_vals[0]
        unsorted_list[min_index] = swapped_vals[1]
        start_index = start_index + 1
        next_index = start_index + 1
        steps+=1
        return selection_sort(unsorted_list, start_index = start_index, next_index = next_index, min_index = start_index, steps = steps)
    else:    
        steps+=1
        if unsorted_list[next_index] < unsorted_list[min_index]:
            min_index = next_index
        next_index+=1
        return selection_sort(unsorted_list, start_index = start_index, next_index = next_index, min_index = min_index, steps = steps)
    
sorted_list = selection_sort([5, 4, 3, 2, 1])
print(sorted_list)