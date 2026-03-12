import csv

# Read from CSV File / Store in List of Dictionaries
def load_students(filename='students_list.csv'):
    database = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = {'id': int(row['id']),
                           'name': row['name'],
                           'grade': int(row['grade'])}
                database.append(student)
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return database

# Add Students to the database
def add_student(database):
    new_id = max([student['id'] for student in database], default = 0) + 1
    while True:
        new_name = input("Enter the student's name (or press Enter to stop): ")
        # if empty name is entered
        if not new_name:
            break
        
        while True:
            try:
                new_grade = int(input("Enter the student's grade (1-5): "))
                if new_grade < 1 or new_grade > 5:
                    print("Invalid grade! Please enter a number between 1 and 5.")
                else:
                    break
            except ValueError:
                print("Invalid input! Please enter a number (1-5)")

        new_student = {'id': new_id, 'name': new_name, 'grade': new_grade}
        database.append(new_student)
        new_id += 1
    return database

# Search for a Student (by ID or name)
def search_student(database, value):
    found = []
    for student in database:
        if str(student['id']) == str(value) or student['name'].lower() == value.lower():
            found.append(student)
    if found:
        for student in found:
            print(f"ID: {student['id']}, Name: {student['name']}, Grade: {student['grade']}")
    else:
        print(f"No student found matching the entered term: {value}")

# Update a Student's grade
def update_grade(database, student_id):
    try:
        student_id = int(student_id)
    except ValueError:
        print("Invalid ID! Please enter a valid ID.")
        return
    
    for student in database:
        if student['id'] == student_id:
            while True:
                try:
                    new_grade = int(input("Enter the new grade: "))
                    if new_grade < 1 or new_grade > 5:
                        print("Invalid grade! Please enter a number between 1 and 5.")
                    else:
                        student['grade'] = new_grade
                        print(f"Grade updated to: {new_grade}")
                        break
                except ValueError:
                    print("Invalid input! Please enter a number (1-5)")
            return
        
    print(f"No student with ID {student_id} found.")

# Save the Database to a CSV File
def save_students(database, filename='students_list.csv'):
    with open(filename, 'w', newline='') as file:
        fieldnames = ['id', 'name', 'grade']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in database:
            writer.writerow(student)
    print("Database saved")