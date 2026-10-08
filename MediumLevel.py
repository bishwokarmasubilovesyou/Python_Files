#QUESTION 1

name = input("Enter your username: ")
username = name.strip().lower().replace(" ", "_")
print ("Username:", username)


#QUESTION 2
marks = [45, 78, 62, 89, 55, 92, 38, 76]

highest = max(marks)
lowest = min(marks)

average = sum(marks) / len(marks)

count = 0

for mark in marks:
    if mark > average:
        count += 1

marks.sort()

print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)
print("Students above average:", count)
print("Ascending order:", marks)

#QUESTION 3

names = ["Ram", "Sita", "Hari", "Ram", "Anu", "Sita", "Mina"]

unique_names = []

for name in names:
    if name not in unique_names:
        unique_names.append(name)

unique_names.sort()

print("Unique names:", unique_names)
print("Total unique students:", len(unique_names))

#QUESTION 4
sentence = input("Enter a sentence: ")

sentence = sentence.strip().lower()

words = sentence.split()

print("Number of words:", len(words))

python_count = words.count("python")
print("Python appears:", python_count, "times")

longest = max(words, key=len)
print("Longest word:", longest)

#QUESTION 5

cart = ["apple", "milk", "bread", "apple", "eggs", "milk"]

new_cart = []

for item in cart:
    if item not in new_cart:
        new_cart.append(item)

new_cart.append("cheese")
new_cart.remove("bread")
new_cart.sort()

print("Final cart:", new_cart)
print("Total items:", len(new_cart))

#QUESTION 6

student = {
    "name": "Ram",
    "age": 19,
    "course": "BCA",
    "marks": 78
}

print("Student information:")
print(student)

# Increase marks by 5
student["marks"] = student["marks"] + 5

# Add status
if student["marks"] >= 40:
    student["status"] = "Pass"
else:
    student["status"] = "Fail"

print("Updated dictionary:")
print(student)

#QUESTION 7

list1 = [10, 20, 30, 40, 50, 60]
list2 = [30, 40, 50, 70, 80, 90]

common = []
only_list1 = []
only_list2 = []

for number in list1:
    if number in list2:
        common.append(number)
    else:
        only_list1.append(number)

for number in list2:
    if number not in list1:
        only_list2.append(number)

print("Common values:", common)
print("Only in list1:", only_list1)
print("Only in list2:", only_list2)



#QUESTION 8

email = input("Enter your email: ")

if "@" in email and "." in email and " " not in email and email[0] != "@":
    print("Valid email")
else:
    print("Invalid email")


#QUESTION 9

sentence = input("Enter a sentence: ")

words = sentence.lower().split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

for word, count in frequency.items():
    print(word, ":", count)


#QUESTION 10

inventory = {
    "apple": 20,
    "banana": 15,
    "mango": 10,
    "orange": 8
}

item = input("Enter item name: ").lower()

if item in inventory:

    sold = int(input("How many items were sold? "))

    inventory[item] = inventory[item] - sold

    if inventory[item] == 0:
        del inventory[item]

    print("Updated inventory:")
    print(inventory)

else:
    print("Item does not exist in inventory.")