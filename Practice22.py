# Write a program to assign grades based on marks using chained conditions (if-elif-else).

marks=float(input("Enter Marks : "))
grade=str(" ")
if (marks >= 90):
    grade="A"
    print("Marks = " , marks , "\nGrade : " , grade )
elif (marks>=80):
    grade="B"
    print("Marks = " , marks , "\nGrade : " , grade )
elif (marks>=70):
    grade="C"
    print("Marks = " , marks , "\nGrade : " , grade )
elif (marks>=60):
    grade="D"
    print("Marks = " , marks , "\nGrade : " , grade )
elif (marks >= 33 ):
    grade="E"
    print("Marks = " , marks , "\nGrade : " , grade )
else:
    grade="F"
    print("Marks = " , marks , "\nGrade : " , grade )
