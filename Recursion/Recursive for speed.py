from quicksort import *

def greatest_three_prod(array):
    sorted_array = quicksort(array)
    product = sorted_array[-1]*sorted_array[-2]*sorted_array[-3]
    return product

print(greatest_three_prod([10,3,1,25,44,100,5]))
