import csv
import os
import getpass

F='students.csv'
def sLoad():
    stu=[]
    if os.path.exists(F):
        with open(F,mode='r',newline='') as file:
            reader=csv.DictReader(file)
            for r in reader:
                stu.append(r)
    return stu

def save_st(students):
    with open(F, mode='w', newline='') as file:
        fieldnames = ['StudentID', 'Name', 'Age', 'Grade']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)

def stu_L(students):
    if not students:
        print("No student records found.")
        return
    print("\nStudent Records:")
    for student in students:
        print(f"ID:{student['StudentID']},Name:{student['Name']},Age:{student['Age']},Grade:{student['Grade']}")

def stu_search(students):
    S_ID=input("Enter Student ID to search: ").strip()
    flag=False
    for student in students:
        if student['StudentID']==S_ID:
            print(f"Student Found: ID: {student['StudentID']}, Name: {student['Name']}, Age: {student['Age']}, Grade: {student['Grade']}")
            flag=True
            break
    if not flag:
        print("Student not found.")

def stu_add(students):
    S_ID=input("Enter Student ID: ").strip()
    for student in students:
        if student['StudentID']==S_ID:
            print("Student ID already exists.")
            return
    n= input("Enter Student Name: ").strip()
    ag = input("Enter Student Age: ").strip()
    gr = input("Enter Student Grade: ").strip()
    students.append({'StudentID':S_ID,'Name':n,'Age':ag,'Grade':gr})
    print("Student added successfully.")

def stu_upd(students):
    S_ID=input("Enter Student ID to update: ").strip()
    for student in students:
        if student['StudentID']==S_ID:
            n=input(f"Enter new name (current:{student['Name']}):").strip()
            ag=input(f"Enter new age (current:{student['Age']}):").strip()
            gr=input(f"Enter new grade (current:{student['Grade']}):").strip()
            if n:
                student['Name']=n
            if ag:
                student['Age']=ag
            if gr:
                student['Grade']=gr
            print("Student record updated.")
            return
    print("Student ID not found.")

def stu_del(students):
    S_ID=input("Enter Student ID to delete:").strip()
    for i, student in enumerate(students):
        if student['StudentID']==S_ID:
            del students[i]
            print("Student record deleted.")
            return
    print("Student ID not found.")

def login():
    print("Welcome to THE STUDENT MANAGEMENT MENU!!")
    while True:
        ch=input("Enter 'login' to log in or 'exit' to quit: ").strip().lower()
        if ch=='exit':
            print("Exiting the system!")
            return False
        elif ch=='login':
            u_name=input("Enter username:")
            passs=input("Enter password :")
            if u_name=='admin' and passs=='password':
                print(f"Login successful. Welcome, {u_name}!")
                return True
            else:
                print("Invalid username or password. Try again.")
        else:
            print("Invalid choice. Please enter 'login' or 'exit'.")

def main():
    if not login():
        return

    students = sLoad()
    while True:
        print("\nStudent Data Management System")
        print("List Students:           (Press 1)")
        print("Search Student:          (Press 2)")
        print("Add Student:             (Press 3)")
        print("Update Student:          (Press 4)")
        print("Delete Student:          (Press 5)")
        print("Exit:                    (Prsss 6)")
        ch = input("Enter your choice (1-6): ").strip()

        if ch=='1':
            stu_L(students)
        elif ch=='2':
            stu_search(students)
        elif ch=='3':
            stu_add(students)
            save_st(students)
        elif ch=='4':
            stu_upd(students)
            save_st(students)
        elif ch=='5':
            stu_del(students)
            save_st(students)
        elif ch=='6':
            print("Exiting the system!")
            break
        else:
            print("Invalid INPUT! Please enter the correct input (1-6):")

main()