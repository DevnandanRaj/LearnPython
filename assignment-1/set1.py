# Print hello world.
print("Hello, World!")

# Data Type Paly
# Integer
number = 1
print(type(number), number)
# float
number2 = 3.14
print(type(number2), number2)
# String
name = "Dev"
print(type(name), name)
# boolean
flag = True
print(type(flag), flag)
# list
my_list = [1, 2, 34, 55]
print(type(my_list), my_list)
# tuple
my_tuple = (1, 2, 34, 55)
print(type(my_tuple), my_tuple)
# dictionary
my_data = {name: "Dev", "age": 24}
print(type(my_data), my_data)
# set
my_set = {1, 2, 3}
print(type(my_set), my_set)

# List oprations
NumberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# added a number to list
NumberList.append(11)
print("added number 11",NumberList)
# Removed a number from list specificly the last number.
NumberList.pop()
print("poped the last item",NumberList)
# sorted the list in descending.
NumberList.sort(reverse=True)
print("lsit in reverse",NumberList)
# Sum of List.
SumList=[10, 20, 30, 40]
sum = sum(SumList)
print("Sum of list",sum)
#Avg of list
average=(sum/len(SumList));
print("Average of list",average)

#String Reversa
stringToReverse="Python";
print("Orignal String",stringToReverse)
reversedString= stringToReverse[::-1]
print("Reversed String",reversedString)

#Count Vowels
CountString="Hello"
vowels="aeiou"
count=0;
for char in CountString:
    if char in vowels:
        count+=1;
        
print("Numbers of vowel",count);
#Prime Number
def  PrimeChek(number):
     if number<=1:
         return False
     if number<=3:
         return True
     if number % 2 ==0 or number % 3==0:
         return False
     i=5
     while i*i<=number:
         if number%i==0 or number%(i+2)==0:
             return False
         i+=6
     return True 
 
number=13;
if PrimeChek(number):
    print(number,"is a prime number")
else:
    print(number,"is not a prime number")
    
    
#Factorial Calculation
def factorialNumber(number):
    if number == 0:
        return 1
    else:
        return number * factorialNumber(number - 1)
n=5
result=factorialNumber(n)
print("Factorial of",n,"is",result)

#Fibonacci Sequence
def fibonachi(number):
    if number <= 0:
        return 0
    elif number==1:
        return 1
    else:
        return fibonachi(number-1)+fibonachi(number-2)
fibn=5
for i in range(fibn):
    print(fibonachi(i), end=", ")  
    

#List Comprehension:
squareList=[x**2 for x in range(1,11)]
print("List comprehension of square",squareList)