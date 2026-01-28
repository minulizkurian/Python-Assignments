# Task 1: Create a Dictionary of Student Marks

# Problem Statement: Write a Python program that:
# 1.   Creates a dictionary where student names are keys and their marks are values.
# 2.   Asks the user to input a student's name.
# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message.
                                                        
student_details={"John":854,"Alice":989,"Carolin":789,"Jay":999}

sname=input("Enter the student's name:")

if sname in student_details:
    print(f"{sname}'s marks: {student_details[sname]}")
else:
    print("Student not found")
