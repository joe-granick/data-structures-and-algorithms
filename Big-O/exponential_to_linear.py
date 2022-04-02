from collections import defaultdict

def exponential_dup(list):
    steps = 0
    for i in range(len(list)):
        for j in range(len(list)):
            steps += 1
            if i != j and list[i] == list[j]:
                return (True, len(list), steps)
    return (False, len(list), steps)

print(exponential_dup([1,2, 3, 4, 4]))
print(exponential_dup([1,2, 3, 4, 5]))


def linear_dup(list):
    steps = 0
    counted = defaultdict(lambda: False)
    for i in range(len(list)):
        steps +=1
        if counted[list[i]]:
            return (True, len(list), steps)
        counted[i] = True
    return (False, len(list), steps)

print(linear_dup([1,2, 3, 4, 4]))
print(linear_dup([1,2, 3, 4, 5]))