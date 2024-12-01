import os
import csv

# Importowanie studentów z pliku
def import_from_file():
    students = []
    try:
        with open('students.csv', 'r', newline='') as file:
            for line in file:
                cut_parts = line.strip().split(',')
                if len(cut_parts) == 2:  # brak statusu obecności
                    students.append({
                        'first_name': cut_parts[0].strip(),
                        'last_name': cut_parts[1].strip(),
                        'present': False
                    })
                elif len(cut_parts) == 3:  # status obecności podany
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

# Eksportowanie obecności
def export_attendance(students):
    with open('students.csv', 'w', newline='') as file:
        for student in students:
            present = 'yes' if student['present'] else 'no'
            file.write(f"{student['first_name']},{student['last_name']},{present}\n")
        