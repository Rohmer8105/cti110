mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))


grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

if average_grade >= 90:
    letter_grade = 'A'
elif average_grade >= 80:
    letter_grade = 'B'
else:
    letter_grade = 'F'

print("\n-----------Results------------")
print("Lowest Grade:", lowest_grade)
print("Highest Grade:", highest_grade)
print("Sum of Grades:", sum_of_grades)
print("Average: {:.2f}".format(average_grade))
print("-----------------------------------------")
print("Your grade is:", letter_grade)
