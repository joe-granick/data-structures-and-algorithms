def insertion_sort(unsorted_list):
    for index in range(1, len(unsorted_list)):
        temp_min = unsorted_list[index]
        position = index-1
        while position >= 0:
            if temp_min < unsorted_list[position]:
                unsorted_list[position+1] = unsorted_list[position]
                position-=1
            else:
                break
            unsorted_list[position+1] = temp_min
          
    return(unsorted_list)

print(insertion_sort([2,4,7,1,3]))

#### BIG O of insertion sort is O(n^2) but performs better than other sort algorithms in the average case, this isn't captured in BigO which only looks at worst case performance