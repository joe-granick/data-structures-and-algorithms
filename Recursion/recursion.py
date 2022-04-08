def char_count(array, count = 0):
    if len(array) == 0:
        return count
    else:
        count+=len(array[0])
        return char_count(array[1:], count)
print(char_count(["ab", "c", "def", "ghij"]))