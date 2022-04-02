
def swap_list(a, b):
    return (b, a)

test = [1, 2, 3 , 4, 5]
print(test)
swapped= swap_list(test[0], test[1])
test[0] = swapped[0]
test[1] = swapped[1]
print(test)


def bubble_sort(unsorted_list, index = 0, list_sorted = True):
    last_index = len(unsorted_list)
    if index+1 < last_index:
        if unsorted_list[index] > unsorted_list[index+1]:
            swapped = swap_list(unsorted_list[index], unsorted_list[index+1])
            unsorted_list[index] = swapped[0]
            unsorted_list[index+1] = swapped[1]
            list_sorted = False
        index+=1
        return bubble_sort(unsorted_list, index, list_sorted)
    elif list_sorted:
        return unsorted_list
    else:
        return bubble_sort(unsorted_list, index = 0, list_sorted = True)
    



bubble_sort_test = bubble_sort([5, 1, 7, 3, 2, 4])
print(len([5, 1, 7, 3, 2, 4]))

print(bubble_sort_test)
        

