# Student Result Management System

print("===== STUDENT RESULT MANAGEMENT =====")

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

subjects = ["Python", "DBMS", "Operating System", "Data Structure", "English"]
marks = []

for subject in subjects:
    mark = float(input(f"Enter marks in {subject}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / len(subjects)

if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 35:
    grade = "D"
else:
    grade = "F"

print("\n========== RESULT ==========")
print("Name:", name)
print("Roll No:", roll_no)
print("Total Marks:", total, "/ 500")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)

if percentage >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")