from quicksort import *

def greatest_three_prod(array):
    sorted_array = quicksort(array)
    product = sorted_array[-1]*sorted_array[-2]*sorted_array[-3]
    return product

print(greatest_three_prod([10,3,1,25,44,100,5]))



def missing_increment(array):
    sorted_array = quicksort(array)
    for index, value in enumerate(sorted_array):
        print(index, value)
        print(sorted_array)
        if index == len(sorted_array)-1:
            return "No missing increments"
            break
        if sorted_array[index+1] != value+1:
            missing_val = value+1
            return missing_val

print(missing_increment([5,3,1,2,6,4]))