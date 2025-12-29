
# WAP TO CREATE A DICTIONARY CONTAINING NAMES OF COMPETITION WNNER STUDENTS
# AS KEYS AND NUMBER OF THIER WINS ARE VALUES.

n=int(input("Enter number of students : "))
compwin={}
for a in range(n):
    name=input("Enter name of student : ")
    win=int(input("Enter number of wins : "))
    compwin[name]=win
print("Now the dictionary is :")
print(compwin)
print(type(compwin))

x=compwin.items()
print(x)

