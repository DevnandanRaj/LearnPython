from itertools import permutations

#1. **Anagram Check**: Write a Python function that checks whether two given words are anagrams.- 
# *Input*: "cinema", "iceman"
word1 = "cinema"
word2 = "iceman"


def anagrams(word1, word2):
    w1 = word1.replace(" ", "").lower()
    w2 = word2.replace(" ", "").lower()
    return sorted(w1) == sorted(w2)


print(anagrams(word1, word2))

# 2. **Bubble Sort**: Implement the bubble sort algorithm in Python.
#     - *Input*: [64, 34, 25, 12, 22, 11, 90]
#     - *Output*: "[11, 12, 22, 25, 34, 64, 90]"
arr = [64, 34, 25, 12, 22, 11, 90]


def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


bubblesort(arr)
print(arr)

# 3. **Longest Common Prefix**: Given a list of strings, find the longest common prefix.
#     - *Input*: ["flower","flow","flight"]
#     - *Output*: "fl"

word = ["flower", "flow", "flight"]


def comprefix(word):
    prefix = ""
    if not word:
        return ""
    word.sort()
    for i in range(len(word[0])):
        if word[0][i] == word[-1][i]:
            prefix += word[0][i]
        else:
            break
    return prefix


print(comprefix(word))

#4. **String Permutations**: Write a Python function to calculate all permutations of a given string.
# - *Input*: "abc"

def string_permutation(str):
    permuted_list=[''.join(p) for p in permutations(str)]
    return permuted_list

result=string_permutation('abc')
print(result)

#5. **Implement Queue using Stack**: Use Python's stack data structure to implement a queue.
#    - *Input*: enqueue(1), enqueue(2), dequeue(), enqueue(3), dequeue(), dequeue()


class QueueUsingStack:
    def __init__(self):
        self.stack_enqueue = []
        self.stack_dequeue = []

    def enqueue(self, data):
        # Push the data onto the enqueue stack
        self.stack_enqueue.append(data)

    def dequeue(self):
        # If both stacks are empty, the queue is empty
        if not self.stack_enqueue and not self.stack_dequeue:
            return None

        # If the dequeue stack is empty, transfer elements from the enqueue stack
        if not self.stack_dequeue:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())

        # Pop the front element from the dequeue stack
        if self.stack_dequeue:
            return self.stack_dequeue.pop()
        else:
            return None  # Return None if the queue is empty


# Example usage
queue = QueueUsingStack()

queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())  # Output: 1

queue.enqueue(3)
print(queue.dequeue())  # Output: 2
print(queue.dequeue())  # Output: 3
print(queue.dequeue())  # Output: None

# Missing Number: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

def missing_num(list):
    list.sort()
    for x in range(len(list) - 1):
        if list[x] + 1 != list[x + 1]:
            return list[x] + 1

result=missing_num([3,0,1])
print(result)

# Climbing Stairs: You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climb_stairs(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for x in range(3, n + 1):
        dp[x] = dp[x - 1] + dp[x - 2]
    return dp[n]

result = climb_stairs(3)
print(result)


#9. **Power of Two**: Given an integer, write a function to determine if it is a power of two.
#    - *Input*: 16

def power_two(n):
    return n > 0 and (n & (n - 1)) == 0

result = power_two(16)
print(result)

# Contains Duplicate: Given an array of integers, find if the array contains any duplicates.
def contains_duplicate(nums):
    unique_set = set()

    for num in nums:
        if num in unique_set:
            return True
        unique_set.add(num)

    return False
result = contains_duplicate([1, 2, 3, 1])
print(result)

# Binary Search: Write a function that implements binary search on a sorted array.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


result = binary_search([1, 2, 3, 4, 5, 6], 4)
print(result)


# Quick Sort: Implement quick sort in Python.

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)


arr = [10, 7, 8, 9, 1, 5]
result = quickSort(arr)
print(result)

# Single Number: Given a non-empty array of integers, every element appears twice except for


def find_non_repeating_number(nums):
    count_dict = {}
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    for num, count in count_dict.items():
        if count == 1:
            return num

    return None  


numbers = [4, 1, 2, 1, 2]
result = find_non_repeating_number(numbers)
print(result)

# Maximum Subarray: Find the contiguous subarray within an array (containing at least one number) which has the largest sum.


def maxSubArray(nums):
    current_sum = max_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum



arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = maxSubArray(arr)
print(result)
