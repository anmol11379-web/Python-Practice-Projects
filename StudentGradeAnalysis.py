
# students = [
#     {"name": "Student1", "grades": [85, 90, 78]},
#     {"name": "Student2", "grades": [58, 65, 70]},
#     {"name": "Student3", "grades": [95, 100, 98]},
#     {"name": "Student4", "grades": [75, 80, 72]}
# ]
# def calculate_average(grades):
#     return sum(grades) / len(grades)
# def assign_grade(avg):
#     if avg >= 90:
#         return "A"
#     elif avg >= 80:
#         return "B"
#     elif avg >= 70:
#         return "C"
#     elif avg >= 60:
#         return "D"
#     else:
#         return "F"
# for student in students:
#     avg = calculate_average(student['grades'])
#     grade = assign_grade(avg)
#     print(f"{student['name']}: Average = {avg:.2f}, Grade = {grade}")


def calculate_average(grades):
    return sum(grades) / len(grades)

def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

students = []
num_students = int(input("Enter the number of students: "))

for _ in range(num_students):
    student = {}
    student['name'] = input("Enter student name: ")
    grades = []
    for i in range(1, 4):
        while True:
            try:
                mark = float(input(f"Enter mark {i} for {student['name']}: "))
                if 0 <= mark <= 100:
                    grades.append(mark)
                    break
                else:
                    print("Please enter a mark between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    student['grades'] = grades
    
    students.append(student)

print("\nStudent Grade Analysis:")
for student in students:
    avg = calculate_average(student['grades'])
    grade = assign_grade(avg)
    print(f"{student['name']}: Average = {avg:.2f}, Grade = {grade}")
