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

