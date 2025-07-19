# Questions 



## Two Sum 

### Intuition

- To solve this problem efficiently, we avoid the brute force approach of trying every possible pair of numbers to see if they add up to the target sum.\
- Instead we use a dictionary (also hash map in other langs) which offers fast look up times (that avgs out to O(1)).

**The basic idea** is to iterate through the list once, and for each number, we check if the number required to reach the target (target - current_number) has already been seen in the array.

<details><summary>Solution</summary>


### Solution Approach

- Initialize an empty hash table (dictionary in Python dialect), we'll call it m.

- Iterate over the nums array, enumerating both the value x and its index i. Enumeration provides a convenient way of getting both the value and the index without additional overhead.

- For every value x, calculate its complement y by subtracting x from target (y = target - x).

- Check if y is present as a key in the hash table. 
  - If it is found, it means we had already seen the necessary pair earlier in the array. We then retrieve m[y], which is the index of y we had stored, and return a list containing the indices of y and x ([m[y], i]). This satisfies the requirement as their sum is equal to the target.

  - If y is not in the hash table, add the current value x along with its index i to the hash table (m[x] = i). This stores x for future reference if we later come across its complement y.

### Code 

```python 
mydict = {}  # {key: index}
    for i in range(0, len(nums)):
        if (target-nums[i]) in mydict:
            return [i, mydict[target-nums[i]]]
        
        mydict[nums[i]] = i
```
</details>


## Reverse Linked List

The task is to reverse a singly linked list. A linked list is a data structure where each element (often called a 'node') contains a value and a pointer/reference to the next node in the sequence. A singly linked list means that each node points to the next node and there is no reference to previous nodes. \
The problem provides a pointer to the head of the linked list, where the 'head' represents the first node in the list. Our goal is to take this linked list and return it in the reversed order. For instance, if the linked list is `1 -> 2 -> 3 -> null`, the reversed list should be `3 -> 2 -> 1 -> null`.

### Intuition 

- The intuition behind this solution is to take each node and move it to the beginning of the new reversed list as we traverse through the original list. 
- We maintain a temporary node, often referred to as a 'dummy' node, which initially points to null, as it will eventually become the tail of the reversed list once all nodes are reversed.

**STEPS:**\
We iterate from the head towards the end of the list, and with each iteration, we do the following:

- Temporarily store the next node (since we are going to disrupt the next reference of the current node).
- Set the next reference of the current node to point to what is currently the first node of the reversed list (initially, this is null or dummy.next).
- Move the dummy's next reference to the current node, effectively placing the current node at the beginning of the reversed list.
- Move to the next node in the original list using the reference we stored earlier.


### Solution Approach

For Complete walthrough: [This Link](https://algo.monster/liteproblems/206)