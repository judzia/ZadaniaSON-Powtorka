import os
import csv

# Importing students from file
def import_from_file():
    students = []
    try:
        with open('students.csv', 'r', newline='') as file:
            for line in file:
                cut_parts = line.strip().split(',')
                if len(cut_parts) == 2:  # attendance status not provided 
                    students.append({
                        'first_name': cut_parts[0].strip(),
                        'last_name': cut_parts[1].strip(),
                        'present': False
                    })
                elif len(cut_parts) == 3:  # attendance status given
                    students.append({
                        'first_name': cut_parts[0].strip(),
                        'last_name': cut_parts[1].strip(),
                        'present': cut_parts[2].strip().lower() == 'yes'
                    })
                else:
                    print('Wystąpił błąd podczas importowania danych.')
        return students
    except FileNotFoundError:
        print("Nie znaleziono pliku 'students.csv'.")
        return []

# Exporting attendance
def export_attendance(students):
    with open('students.csv', 'w', newline='') as file:
        for student in students:
            present = 'yes' if student['present'] else 'no'
            file.write(f"{student['first_name']},{student['last_name']},{present}\n")
        
# Adding new student
def add_student():
    first_name = input("Podaj imię studenta: ")
    last_name = input("Podaj nazwisko studenta: ")
    with open('students.csv', 'a', newline='') as file:
        writer = csv.writer(file) # creating object writer
        writer.writerow([first_name, last_name, 'no'])  # saving info about new student
    print(f"Student {first_name} {last_name} został dodany.")


# Editing info about students
def edit_student():
    old_first_name = input("Podaj imię studenta do edycji: ")
    old_last_name = input("Podaj nazwisko studenta do edycji: ")
    new_first_name = input("Podaj nowe imię studenta: ")
    new_last_name = input("Podaj nowe nazwisko studenta: ")

    students = import_from_file()
    for student in students:
        if student['first_name'] == old_first_name and student['last_name'] == old_last_name:
            student['first_name'] = new_first_name
            student['last_name'] = new_last_name
            break
    export_attendance(students)
    print(f"Zaktualizowano dane studenta: {new_first_name} {new_last_name}.")

