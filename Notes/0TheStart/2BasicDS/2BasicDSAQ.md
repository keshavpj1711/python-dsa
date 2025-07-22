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

## Number of Recent Calls

In this problem, you are tasked with designing a RecentCounter class that tracks the number of requests received within a specific time frame. The time frame in question is the last 3000 milliseconds, which equates to the last 3 seconds. \
This can be likened to monitoring network traffic, where you're interested in understanding the number of events or requests that have occurred in a sliding window of time for performance analysis or rate limiting.

The class should support two operations:

- `RecentCounter()` is the constructor that initializes the counter. When a RecentCounter object is created, it starts with zero recent requests.
- `ping(int t)` is a method that is called each time a new request is received. 
  - The request comes with a timestamp t (in milliseconds), which is strictly increasing with each call. 
  - The purpose of ping is to add the new request and then return the count of all recent requests within the last 3000 milliseconds, which is the time range from t - 3000 to t, inclusive of both ends of the interval.


### Intuition

The key to solving this problem is to maintain a dynamic list of timestamped requests, ensuring that only those within the last 3000 milliseconds are counted. Because the input guarantees that each t in ping is increasing, we can use a queue to keep track of the timestamps of the recent requests.

**The intuition for using a queue comes from its FIFO (First-In-First-Out) property**, which naturally aligns with the progression of time in our problem. When a new request arrives with timestamp t, we add it to the end of the queue. Then we need to remove all requests from the front of the queue that are outside the 3000 millisecond window (i.e., older than t - 3000).

By doing so, our queue always contains only those requests that are within the 3000 millisecond window. The length of the queue after this cleaning process gives us the number of recent requests, which is what the ping method returns.

To implement this idea in code, we utilize the deque data structure from Python's collections module because it allows for efficient addition and removal of elements from both ends.

### Solution Approach

To view the complete solution: [This Link](https://algo.monster/liteproblems/933)

A simple walkthrough to get the solution is provided below and for this example, assume we receive a sequence of timestamped requests at the following times (in milliseconds): 1, 100, 3001, 3002

- We create a **RecentCounter** object.
- We call `ping(1)`. The deque now has one element: [1].
  - Since there are no pings older than 3000 milliseconds, we return len(self.q) which is 1.
- Next, we call `ping(100)`. The deque becomes: [1, 100].
  - Both pings are within 3000 milliseconds from the current ping time, so the number of recent requests is 2.
- Then we call `ping(3001)`. The deque is updated to: [1, 100, 3001].
  - Now, we check for timestamps older than 3001 - 3000 which is 1. Since 1 is within the range, we do not remove it. The deque remains [1, 100, 3001].
  - The len(self.q) now returns 3, as these are the recent pings within the last 3000 milliseconds.
- Lastly, we call ping(3002). The deque first receives the timestamp 3002: [1, 100, 3001, 3002].
  - We then remove any timestamps older than 3002 - 3000, which is 2. After removal, the deque is [100, 3001, 3002].
  - We return len(self.q), which is 3, as the count of recent requests.


When popping the unecessary elements using while loop, MAIN USE of deque comes that is to pop elements from start.

## Valid Parantheses

The problem presents a scenario in which we are given a string s consisting of six possible characters: the opening and closing brackets of three types—parentheses (), square brackets [], and curly braces {}. The challenge is to determine whether this string represents a sequence of brackets that is considered valid based on certain rules. A string of brackets is deemed valid if it satisfies the following conditions:

- Each opening bracket must be closed by a closing bracket of the same type.
- Opening brackets must be closed in the correct order. That means no closing bracket should interrupt the corresponding pair of an opening bracket.
- Each closing bracket must have an associated opening bracket of the same type before it.

### Intuition

We create a Stack, then we only put the brackets with the open end inside of it, and for it's closed counterpart we pop the bracket. By the end of traversal if the Stack remains empty the given input is a valid parantheses.

### Time and Space Complexity

- The time complexity of the given code is O(n), where n is the length of the input string. This is because the algorithm iterates over each character in the input string exactly once.

- The space complexity of the code is also O(n), as in the worst case (when all characters in the input string are opening brackets), the stack stk will contain all characters in the input string.


## Array Partition

Given an integer array `nums` of `2n` integers, group these integers into `n` pairs `(a1, b1), (a2, b2), ..., (an, bn)` such that the sum of `min(ai, bi)` for all `i` is maximized. Return the maximized sum.

In Simple Words:
- We need to create pairs from the elements in array
- Calculate min of each pair
- Finally, Calculate and return the sum of all these min vals 

> The most important thing here is to construct these pairs wisely in order to get the maximum sum of the minimums from the pair.