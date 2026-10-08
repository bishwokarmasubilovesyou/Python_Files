highest = None
lowest = None
total = 0
passed = 0
failed = 0

for i in range(5):

    mark = float(input("Enter mark for student: "))

    if mark < 0 or mark > 100:
        print("Invalid mark")

    else:

        if mark >= 90:
            grade = "A"

        elif mark >= 80:
            grade = "B"

        elif mark >= 70:
            grade = "C"

        elif mark >= 60:
            grade = "D"

        else:
            grade = "F"

        print("Grade:", grade)

        total += mark

        if mark >= 40:
            passed += 1
        else:
            failed += 1

        if highest is None or mark > highest:
            highest = mark

        if lowest is None or mark < lowest:
            lowest = mark

print("Highest mark:", highest)
print("Lowest mark:", lowest)
print("Average mark:", total / 5)
print("Number of students passed:", passed)
print("Number of students failed:", failed)