def reverse_string(string, stack = ""):
    if len(string) == 0:
        return stack
    else:
        move_char = string[-1]
        stack = stack + move_char 
        return reverse_string(string[:-1], stack)

print(reverse_string("abcde"))

def aVeryBigSum(ar):
    tot = 0
    n = ar[0]
    for i in range(1, len(ar)):
        tot = tot + i
    return n* 100000000 + tot
    

print(aVeryBigSum([5, 1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))
    
        