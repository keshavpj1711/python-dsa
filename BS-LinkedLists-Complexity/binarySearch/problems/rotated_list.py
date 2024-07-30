# You are given list of numbers, obtained by rotating a sorted list an unknown number of times. 
# Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. 
# Your function should have the worst-case complexity of O(log N), where N is the length of the list. 
# You can assume that all the numbers in the list are unique.

# Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.

# We define "rotating a list" as removing the last element of the list and adding it before the first element. 
# E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].

# "Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].


tests = [
  {
    "input": [11, 5, 6, 9],
    "output": 1 # rotations 
  }, 
  {
    "input": [5, 6, 9, 0, 2, 3, 4],
    "output": 3 # rotations 
  }, 
  {
    "input": [12, 23, 28, 40, 5],
    "output": 4 # rotations 
  }, 
  {
    "input": [5, 6, 9, 0, 2, 3, 4],
    "output": 3 # rotations 
  },
  {
    "input": [5],
    "output": 0 # rotations 
  },
  {
    "input": [],
    "output": 0 # rotations 
  },
]

def get_rotations_linear(nums):
  position = 0
  
  while position<len(nums):

    if position > 0 and nums[position] < nums[position-1]:
      return position

    position += 1

  return 0

def get_rotations_bs(nums):
  # Logic
  # If the middle element is smaller than the last element then the smallest element would be to the left
  # If the middle element is larger than the last element then the smallest element would be to the right

  # Pseudocode for this 
  # get the middle element
  # check that with last element
    # if larger you have to go right
    # if smaller then you have to go left

  lo, hi = 0, len(nums)-1
  
  while lo <= hi:
    mid = (lo+hi) // 2 
    mid_number = nums[mid]

    # print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number, ", last_number", nums[hi])

    if mid > 0 and nums[mid] < nums[mid-1]:
      return mid
    elif mid_number < nums[hi]:
      hi = mid-1
    else:
      lo = mid+1

  return 0

if __name__ == "__main__":
  for test in tests:
    rotations = get_rotations_bs(test["input"])
    if rotations == test["output"]:
      print("Passed")
    else:
      print(f"Failed: {test["input"]}, Expected {test["output"]}, Got {rotations} ")