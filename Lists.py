#QUESTION 1

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

# 1. Print complete list
print(fruits)

# 2. Print first fruit
print(fruits[0])

# 3. Print last fruit
print(fruits[-1])

# 4. Print second and third fruits
print(fruits[1:3])

# 5. Print number of fruits
print(len(fruits))


#QUESTION 2
students = ["Ram", "Sita", "Hari", "Gita", "John"]

# 1. Add Sam to the end
students.append("Sam")

# 2. Add Anita to the beginning
students.insert(0, "Anita")

# 3. Add Peter at index 3
students.insert(3, "Peter")

# 4. Print updated list
print(students)

# 5. Print total number of students
print(len(students))

#QUESTION 3

colors = ["Red", "Blue", "Green", "Yellow", "Black"]

# 1. Change Blue to Purple
colors[1] = "Purple"

# 2. Change Black to White
colors[4] = "White"

# 3. Remove Green
colors.remove("Green")

# 4. Remove last item
colors.pop()

# 5. Print final list
print(colors)

#QUESTION 4

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 1. First five numbers
print(numbers[:5])

# 2. Last five numbers
print(numbers[-5:])

# 3. Index 2 to 6
print(numbers[2:7])

# 4. Every second number
print(numbers[::2])

# 5. Reverse order
print(numbers[::-1])

#QUESTION 5

numbers = [12, 5, 8, 20, 15, 3, 10]

number = int(input("Enter a number: "))

if number in numbers:
    print(number, "is present in the list.")
else:
    print(number, "is not present in the list.")

#QUESTION 6
numbers = [15, 25, 10, 30, 20, 5]

total = sum(numbers)
smallest = min(numbers)
largest = max(numbers)
average = total / len(numbers)
count = len(numbers)

print("Total:", total)
print("Smallest:", smallest)
print("Largest:", largest)
print("Average:", average)
print("Number of elements:", count)


#QUESTION 7

languages = ["Python", "Java", "C", "JavaScript", "C++"]

for language in languages:
    print(language)

for language in languages:
    print("I am learning", language)

for language in languages:
    print(language, "-", len(language), "characters")


#QUESTION 8

numbers = [45, 12, 78, 3, 56, 23, 89, 10]

# 1. Original list
print("Original:", numbers)

# 2. Ascending order
numbers.sort()
print("Ascending:", numbers)

# 3. Descending order
numbers.sort(reverse=True)
print("Descending:", numbers)

# 4. Smallest number
print("Smallest:", min(numbers))

# 5. Largest number
print("Largest:", max(numbers))

# Sort names alphabetically
names = ["Ram", "Sita", "Hari", "Gita", "John"]
names.sort()
print("Names:", names)

#QUESTION 9

numbers = [10, 20, 10, 30, 20, 40, 10, 50, 30]

new_list = []

for number in numbers:
    if number not in new_list:
        new_list.append(number)

print(new_list)


#QUESTION 10

marks = [75, 82, 68, 90, 55, 88, 72, 95]

# 1. Print all marks
print("Marks:", marks)

# 2. Total marks
print("Total:", sum(marks))

# 3. Average marks
print("Average:", sum(marks) / len(marks))

# 4. Highest mark
print("Highest:", max(marks))

# 5. Lowest mark
print("Lowest:", min(marks))

# 6. Count students who scored 75 or more
count = 0

for mark in marks:
    if mark >= 75:
        count += 1

print("Students scoring 75 or more:", count)

# 7. Sort highest to lowest
marks.sort(reverse=True)
print("Highest to lowest:", marks)

