# We need to write a program to find the position of a given number in a list of numbers arranged in decreasing order.
# We also need to minimize the number of times we access elements from the list.

# Listing the test cases
# - The element is found
# - The element is not found
# - The list is empty
# - The list contains multiple instances of target

tests = [
    {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
    {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
    {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
    {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
    {'input': {'cards': [6], 'query': 6}, 'output': 0},
    {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
    {'input': {'cards': [], 'query': 7}, 'output': -1},
    {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3}, 'output': 7},
    {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 6}, 'output': 2}
]


def locate_number(list, target):
  # Writing a pseudo code 
  # Find the middle element
  # Check if that element is bigger or smaller than target
  # if smaller, pick the middle element from the left half of the list, considering the list is sorted in descending order
  # if bigger, pick the middle element from the right half of the list
  # if no more elements return -1, if element found return it's position
  lo, hi = 0, len(list) - 1

  while lo <= hi:
    mid = (lo + hi) // 2 
    mid_no = list[mid]

    if mid_no == target:
      return mid
    elif mid_no < target:
      ho = mid-1
    else:
      lo = mid+1

  return -1

if __name__=="__main__":
  for test_case in tests:
    locate_number(**test)


