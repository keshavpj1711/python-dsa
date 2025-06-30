# Given an ascending order sorted array to find the starting and end position of a query
# Input: 
#   nums: [1, 3, 5, 5, 9] and query: 5
# Output: [start_position, end_position]
#   output: [2, 3]
# On Leetcode: 34. Find First and Last Position of Element in Sorted Array


def get_start_position(nums, target):
    # this is the main logic which decides which part of the array is to be selected
    def condition(mid):
        mid_number = nums[mid]
        if mid_number == target:
            # checking if there's a element before the found element
            if mid-1 >= 0 and nums[mid-1] == target:
                return 'left'
            else: 
                return 'found'
        elif mid_number < target: 
            return 'right'
        elif mid_number > target: 
            return 'left'

    # below here we have the generic implementation of the binary search
    lo, hi = 0, len(nums)-1
    while lo <= hi:
        mid = (lo + hi)//2
        result = condition(mid)
        if result == 'found': 
            return mid
        elif result == 'left':
            hi = mid -1
        elif result == 'right':
            lo = mid +1
    
    return -1

def get_end_position(nums, target):
    def condition(mid):
        mid_number = nums[mid]
        # checking if there's an element after the found element
        if mid_number == target:
            if mid+1 <= len(nums) -1 and nums[mid+1] == target:
                return 'right'
            else: 
                return 'found'
        elif mid_number < target: 
            return 'right'
        elif mid_number > target: 
            return 'left'

    lo, hi = 0, len(nums)-1
    while lo <= hi:
        mid = (lo + hi)//2
        result = condition(mid)
        if result == 'found': 
            return mid
        elif result == 'left':
            hi = mid -1
        elif result == 'right':
            lo = mid +1

    return -1
 
def get_positions(nums, target): 
    return [get_start_position(nums, target), get_end_position(nums, target)]

print(get_positions([1, 3, 5, 5, 9, 9], 2))
print(get_positions([2, 2], 2))