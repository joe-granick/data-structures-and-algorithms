def reverse_string(string, stack = ""):
    if len(string) == 0:
        return stack
    else:
        move_char = string[-1]
        stack = stack + move_char 
        return reverse_string(string[:-1], stack)

print(reverse_string("abcde"))

    
        