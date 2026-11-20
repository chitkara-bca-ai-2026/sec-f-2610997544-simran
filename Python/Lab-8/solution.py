print("=== SCHOOL RESULT PROCESSING ===")

student_name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")

total_marks = 0
failed_subject = False

for subject in range(1, 6):
    marks = int(input("Enter marks for Subject " + str(subject) + " (0-100): "))

    if marks < 0 or marks > 100:
        print("Invalid marks. Please enter marks from 0 to 100.")
        marks = int(input("Enter marks for Subject " + str(subject) + ": "))

    total_marks = total_marks + marks

    if marks < 40:
        failed_subject = True

percentage = total_marks / 5

if failed_subject:
    result = "FAIL"
    grade = "F"
    remarks = "Failed in one or more subjects"
elif percentage >= 90:
    result = "PASS"
    grade = "A+"
    remarks = "Outstanding"
elif percentage >= 80:
    result = "PASS"
    grade = "A"
    remarks = "Excellent"
elif percentage >= 70:
    result = "PASS"
    grade = "B"
    remarks = "Very Good"
elif percentage >= 60:
    result = "PASS"
    grade = "C"
    remarks = "Good"
elif percentage >= 50:
    result = "PASS"
    grade = "D"
    remarks = "Satisfactory"
else:
    result = "PASS"
    grade = "E"
    remarks = "Pass"

print("\n=== STUDENT REPORT CARD ===")
print("Student Name:", student_name)
print("Roll Number:", roll_number)
print("Total Marks:", total_marks, "/ 500")
print("Percentage:", percentage, "%")
print("Result:", result)
print("Grade:", grade)
print("Remarks:", remarks) 