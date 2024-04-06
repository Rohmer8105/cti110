# Ryan Rohme
# March 10, 2024
# P2HW2
# Assignment assess student understanding of Lists

# 1. Initialize an empty list to store the grades.
# 2. Ask the user to enter grades for each module and append them to the list.
# 3. Calculate the lowest grade, highest grade, sum of grades, and average grade.
# 4. Display the results with proper formatting.

grades = []

grades.append(float(input("Enter grade for module 1: ")))
grades.append(float(input("Enter grade for module 2: ")))
grades.append(float(input("Enter grade for module 3: ")))
grades.append(float(input("Enter grade for module 4: ")))
grades.append(float(input("Enter grade for module 5: ")))
grades.append(float(input("Enter grade for module 6: ")))

lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

print("\n------------Results------------")
print("Lowest grade:", lowest_grade)
print("Highest grade:", highest_grade)
print("Sum of grades:", sum_of_grades)
print("Average: {:.2f}".format(average_grade))
print("---------------------------------")
