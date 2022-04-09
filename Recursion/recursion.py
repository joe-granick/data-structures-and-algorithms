def char_count(array, count = 0):
    if len(array) == 0:
        return count
    else:
        count+=len(array[0])
        return char_count(array[1:], count)
print(char_count(["ab", "c", "def", "ghij"]))

def evens(nums, even_nums = []):
    if len(nums) == 0:
        return even_nums
    else:
        check_num = nums[0]
        if check_num%2 ==0:
            even_nums.append(check_num)
        return evens(nums[1:], even_nums)
print(evens([1,2,3,4,5,6,7,8,9,10]))


def triangular_nums(n, tot = 0, index = 1):
    if index > n:
        return tot
    else:
        tot+=index
        index+=1
        return triangular_nums(n, tot, index)

print(triangular_nums(7))

def find_x(string, index = 0):
    if string[0] is 'x':
        return index
    else:
        index+=1
        return find_x(string[1:], index)
print(find_x("abcdefghijklmnopqrstuvwxyz"))

def count_shortest_paths(rows, cols, x0 = 1, y0 = 1):
    if x0 == cols and y0 == rows:
        return 1
    else:
        move_x = x0 + 1
        move_y = y0 + 1
        if move_x > cols and move_y <= rows:
            return count_shortest_paths(rows, cols, x0, move_y)
        if move_y > rows and move_x <= cols:
            return count_shortest_paths(rows, cols, move_x, y0)
        return count_shortest_paths(rows, cols, move_x, y0) + count_shortest_paths(rows, cols, x0, move_y)

        
  

print(count_shortest_paths(3, 7))


def count_unique_paths(rows, cols):
    if rows == 1 or cols == 1:
        return 1
    else:
        return count_unique_paths(rows-1, cols) + count_unique_paths(rows, cols-1)

print(count_unique_paths(2, 7))