from aaip.ex2 import load_students, add_student, search_student, update_grade, save_students

# Load Students from 'students_list.csv'
students_db = load_students()

# Add Student's to the Database
print("Adding a New Student!")
students_db = add_student(students_db)

# Search for Student (by ID or Name)
print("Searching for a Student!")
search_term = input("Enter a student name or ID to search: ")
search_student(students_db, search_term)

# Update a student's grade
print("Updating the Grade of a Student!")
student_id = input("Enter the ID of the student to update the grade: ")
update_grade(students_db, student_id)

# Save the updated Database as 'students_list.csv'
save_students(students_db)
