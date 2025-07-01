# We are given, a rotated sorted array -> sorted array which is rotated k number of times 
# [4, 5, 6, 1, 2] -> rotated 3 times from right to left
# We need to find the position of the target element in this rotated sorted array
# Leetcode: 33. Search in Rotated Sorted Array

# After struggling with this problem i found that best solution would be: 
# Look for two sorted arrays and find the element in each using binary search seperately 

def get_position_rotated(nums, target):
  def condition_for_position(mid):
    print("getting position")
    mid_no = nums[mid]

    if mid_no == target:
      return 'found'
    elif target > mid_no:
      return 'right'
    elif target < mid_no:
      return 'left'

  def condition_for_rotation(mid):
    print("getting rotation")
    mid_no = nums[mid]

    if mid-1 >= 0 and mid_no < nums[mid-1]:
      return 'found'
    elif mid_no < nums[-1]:
      return 'left'
    elif mid_no > nums[-1]:
      return 'right'
    else:
      return 'found'

  # First getting if the list is rotated or not
  lo, hi = 0, len(nums)-1
  no_of_rotation = 0
  while lo<=hi:
    mid = (lo+hi)//2
    result = condition_for_rotation(mid)
    print(result)
    
    if result == 'found':
      no_of_rotation = mid
      break
    elif result == 'left':
      hi = mid-1
    elif result == 'right': 
      lo = mid+1
  
  if no_of_rotation == 0:
    lo, hi = 0, len(nums) -1
    while lo<=hi:
      mid = (lo+hi)//2
      result = condition_for_position(mid)
      
      if result == 'found':
        return mid
      elif result == 'left':
        hi = mid-1
      elif result == 'right': 
        lo = mid+1
    
    return -1

  else: 
    lo1, hi1 = 0, no_of_rotation-1
    while lo1<=hi1:
      mid = (lo1+hi1)//2
      result = condition_for_position(mid)
      
      if result == 'found':
        return mid
      elif result == 'left':
        hi1 = mid-1
      elif result == 'right': 
        lo1 = mid+1
    
    lo2, hi2 = no_of_rotation, len(nums)-1
    while lo2<=hi2:
      mid = (lo2+hi2)//2
      result = condition_for_position(mid)
      
      if result == 'found':
        return mid
      elif result == 'left':
        hi2 = mid-1
      elif result == 'right': 
        lo2 = mid+1

    return -1

    


print(get_position_rotated([4,5,6,7,8,1,2,3], 0))
print("------------------")
print(get_position_rotated([], 4))