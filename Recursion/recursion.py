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