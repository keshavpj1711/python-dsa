# Problems to Review

- search rotated list - [Here](./search_rotated_list.py)
- start end index - [Here](./start_end_index.py)

# Concepts to remember 

We already know what binary search is, but a few things to remember for this is 

## First or Last Occurence

In order to find the first and last occurence of an element in a sorted array(in the example below ascending order), we apply the following conditions

The below code is from the condition fn that was defined inside of the the get_start_position() and get_end_position()

```python 
# For first occurence
if mid_number == target:
    if mid-1 >= 0 and nums[mid-1] == target:
        return 'left'
    else: 
        return 'found'

# For last occurence 
if mid_number == target:
    if mid+1 <= len(nums) -1 and nums[mid+1] == target:
        return 'right'
    else: 
        return 'found'
```

## Searching in Rotated Sorted Array

Since here we will have two sorted arrays what we can do is find the element in both of them seperately.

# Optional Question

## Handling repeating numbers
So far we've assumed that the numbers in the list are unique. 
What if the numbers can repeat? E.g. [5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3, 3, 4, 4]. 
Can you modify your solution to handle this special case?

## Searching in a Rotated List
You are given list of numbers, obtained by rotating a sorted list an unknown number of times. 
You are also given a target number. 
Write a function to find the position of the target number within the rotated list. 
You can assume that all the numbers in the list are unique.

Example: In the rotated sorted list [5, 6, 9, 0, 2, 3, 4], the target number 2 occurs at position 5.
