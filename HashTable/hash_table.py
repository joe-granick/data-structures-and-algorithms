from collections import defaultdict
from xml.sax import default_parser_list

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

def duplicate_string(string):
    chars = defaultdict(lambda: False)
    for char in string:
        if chars[char]:
            return char
            break
        else:
            chars[char] = True
    return "No duplicates"

print(duplicate_string(["a", "b", "c", "d", "c", "e", "d"]))
print(duplicate_string(["a", "b", "c", "d"]))

def alphabet_less_one(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    string_letters = defaultdict(lambda: False)
    for char in string:
        string_letters[char] = True
    for char in alphabet:
        if string_letters[char] == False:
            return char
            break
    return ('No letters missing')

print(alphabet_less_one("the quick brown box jumps over the lazy dog"))

def non_dup_char(string):
    string_hash = defaultdict(lambda: 0)
    for char in string:
        string_hash[char] += 1
    for char in string:
        if string_hash[char] == 1:
            return char
            break
    return "No unique characters"
    

print(non_dup_char("minimum"))
    