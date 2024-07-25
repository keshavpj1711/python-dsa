# We need to write a program to find the position of a
# given number in a list of numbers arranged in decreasing order.
# We also need to minimize the number of times we access elements from the list.

import time


def locate_number(list, target):
  for i in range(0, len(list)):
    if list[i] == target:

      print(f"Found {target}")
      return i+1 # returning the position


if __name__ == "__main__":
    list = [13, 11, 10, 7, 4, 3, 1, 0]
    start_time = time.time()
    print(f"Position: {locate_number(list, 7)}")
    end_time = time.time()
    print(f"Runtime: {end_time-start_time}")
