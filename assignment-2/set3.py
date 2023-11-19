#Tuple Unpacking:
list1= [("John", 25), ("Jane", 30)]
for x in list1:
    name,age=x
    print(f"{name} is {age} years old")
    
#Dictionary Manipulation

people_dict={}

def addName(name,age):
    people_dict[name]=age

def updateAge(name, age):
    if name in people_dict:
        people_dict[name] = age
    else:
        print(f"{name} not found in the dictionary.")
        
def deleteName(name):
    if name in people_dict:
        del people_dict[name]
    else:
        print(f"{name} not found in the dictionary.")

# Add name and age
addName("John", 25)
print("After adding John:", people_dict)

# Update the age of a name
updateAge("John", 26)
print("After updating John Age to 26:", people_dict)

# Delete a name from the dictionary
deleteName("John")
print("After deleting John:", people_dict)


#Two Sum Problem
def two_sum(nums, target):
    index = {}  

    for x, num in enumerate(nums):
        complement = target - num
        if complement in index:
            return [index[complement], x]  
        index[num] = x

    return None

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
if result:
    print(f"The indices of the two numbers are: {result[0]} and {result[1]}")
else:
    print("No solution found.")

#Palindrome Check:
str="madama"
bag=""
for x in str:
    bag=x+bag

if bag==str:
    print(f"The word {str} is a palindrome.")
else:
     print(f"The word {str} is not a palindrome.")
     
#Selection Sort
def selection_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for x in range(n):
        # Find the minimum element in the remaining unsorted array
        min_index = x
        for i in range(x + 1, n):
            if arr[i] < arr[min_index]:
                min_index = i
        
        # Swap the found minimum element with the first element
        arr[x], arr[min_index] = arr[min_index], arr[x]

arr = [64, 25, 12, 22, 11]

selection_sort(arr)
print("sorted array",arr)

#Implement Stack using Queue
from queue import Queue
class StackWithQueue:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, data):
        # Add the new element to the first queue
        self.queue1.put(data)

    def pop(self):
        if self.is_empty():
            return None

        # Move all elements from queue1 to queue2 except the last one
        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())

        # The last element in queue1 is the one to be removed (i.e., the top of the stack)
        top_element = self.queue1.get()

        # Swap queue1 and queue2 so that queue1 always contains the elements of the stack
        self.queue1, self.queue2 = self.queue2, self.queue1

        return top_element

    def top(self):
        if self.is_empty():
            return None

        top_element = None
        while not self.queue1.empty():
            top_element = self.queue1.get()
            self.queue2.put(top_element)

        # Swap queue1 and queue2 to maintain the original order
        self.queue1, self.queue2 = self.queue2, self.queue1

        return top_element

    def is_empty(self):
        return self.queue1.empty()


stack = StackWithQueue()

stack.push(1)
stack.push(2)
stack.pop()
stack.push(3)
stack.pop()
stack.pop()
print(stack.top())

#FizzBuzz

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz", end=", ")
    elif number % 3 == 0:
        print("Fizz", end=", ")
    elif number % 5 == 0:
        print("Buzz", end=", ")
    else:
        print(number, end=", ")
        
#File I/O: 
# Open the input file for reading
with open("input.txt", "r") as file:
    content = file.read()

# Split the content into words using whitespace as the delimiter
words = content.split()

# Count the number of words
word_count = len(words)

# Create a string with the word count
output_content = f"Number of words: {word_count}"

# Write the word count to the output file
with open("output.txt", "w") as output_file:
    output_file.write(output_content)
    
#Exception Handling
def divideNumbers(a, b):
    try:
        div = a / b
        return div
    except ZeroDivisionError:
        return "Cannot divide by zero."


num1 = 5
num2 = 0

output = divideNumbers(num1, num2)
print(output)  