from collections import defaultdict

def intersection(array1, array2):
    big_array_dict = defaultdict(lambda: False)
    intersect =[]
    if len(array1) >= len(array2):
        big_array = array1
        small_array = array2
    else:
        big_array = array2
        small_array = array1
    for val in big_array:
        big_array_dict[val] = True
    for val in small_array:
        if big_array_dict[val]:
            intersect.append(val)
    return(intersect)

print(intersection([1,2,3,4,5], [0,2,4,6,8]))


    
    