def add_until_100(array):
    if len(array) == 0:
        return 0
    else:
        added_to_100 = add_until_100(array[1:])
        if array[0] + added_to_100 > 100:
            return added_to_100
        else:
            return array[0] + added_to_100

print(add_until_100([25, 40, 20, 15]))

def golomb(n, memo = {}):
    if n == 1:
        return 1
    else:
        if n not in memo:
            memo[n] = 1 + golomb(n- golomb(golomb(n-1,memo), memo), memo)

        return memo[n]


print(golomb(100))

def unique_paths(rows, cols, memo = {}):
    if rows == 1 or cols == 1:
        return 1
    else:
        if (rows, cols) not in memo:
            memo[(rows,cols)] = unique_paths(rows-1, cols, memo) + unique_paths(rows, cols-1, memo)
        return memo[(rows, cols)]

print(unique_paths(2,7))