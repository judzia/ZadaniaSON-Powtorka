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

    if not first_name or not last_name:
        raise ValueError("Imię i nazwisko są wymagane!")
    
    with open('students.csv', 'a', newline='') as file:
        file.write(f"{first_name},{last_name},no\n")
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


# Editing attendance 
def edit_attendance():
    student_name = input("Podaj imię i nazwisko studenta (np. Jan Kowalski): ")
    students = import_from_file()
    found = False  # whether the student was found

    for student in students:
        if f"{student['first_name']} {student['last_name']}" == student_name:
            found = True
            status = input(f"Obecność dla {student_name} (tak/nie): ").strip().lower()
            student['present'] = (status == 'tak')
            print(f"Obecność dla {student_name} została zaktualizowana.")
            break

    if not found:
        print(f"Student {student_name} nie istnieje w bazie danych.")

    export_attendance(students)


# Menu 
def menu():
    while True:
        print("\nMENU:")
        print("1. Importuj studentów")
        print("2. Eksportuj obecności")
        print("3. Dodaj studenta")
        print("4. Edytuj dane studenta")
        print("5. Edytuj obecność studenta")
        print("6. Zakończ")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            students = import_from_file()
            print("Zaimportowani studenci:", students)
        elif choice == "2":
            students = import_from_file()
            export_attendance(students)
            print("Obecności zostały wyeksportowane.")
        elif choice == "3":
            add_student()
        elif choice == "4":
            edit_student()
        elif choice == "5":
            edit_attendance()
        elif choice == "6":
            print("Koniec programu.")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


if __name__ == "__main__":
    menu()
