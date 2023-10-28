#### Problem **1: Print the following pattern**

pattern="";
for x in range(1,6):
    for i in range(1,x+1):
        pattern+=str(i)+" "
    pattern+="\n"
print(pattern)

#Display numbers from a list using loop

numbers=[12, 75, 150, 180, 145, 525, 50]
for x in range(len(numbers)):
    if numbers[x] % 5==0 and numbers[x]<=150:
        print(numbers[x])
    if numbers[x]>500:
        break;
    if numbers[x]>150:
        continue;
    
#Append new string in the middle of a given string

s1="Aulty";
s2="Kelly";
mid=len(s1)//2
s3=s1[:mid]+ s2 +s1[mid:]
print(s1)
print(s2)
print("New string with inseted sting in the middle",s3)

#### **Arrange string characters such that lowercase letters should come first**

str1="PyNaTive"
print(str1)
lowercase = ""
uppercase = ""

for char in str1:
    if char.islower():
        lowercase += char
    else:
        uppercase += char

str2 = lowercase + uppercase

print("New string",str2)

#Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

list3 = [list1[i] + list2[i] for i in range(min(len(list1), len(list2)))]
print(" Concatenate two lists index-wise",list3)

#Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

list3 = [x + y for x in list1 for y in list2]
print("Concatenated list in the following order",list3)

# Iterate both lists simultaneously

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for x, i in zip(list1,reversed(list2)):
    print(x,i)
    
#Initialize dictionary with default values

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
result = {employee: defaults.copy() for employee in employees}
print(result);

#Create a dictionary by extracting the keys from a given dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

extractedKeys = {key: sample_dict[key] for key in keys}
print(extractedKeys);

#Modify the tuple
tuple1 = (11, [22, 33], 44, 55)
list1 = list(tuple1)
list1[1][0] = 222
tuple1 = tuple(list1)
print(tuple1)
