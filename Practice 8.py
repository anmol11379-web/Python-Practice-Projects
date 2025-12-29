# WAP to find the greatest of 3 numbers entered by the user.

a=int(input("Enter number 1 : "))
b=int(input("Enter number 2 : "))
c=int(input("Enter number 3 : "))
if a>b and c :
    print("Number 1 is greatest.")
elif b>a and c :
    print("Number 2 is greatest.")
elif c>a and b :
    print("Number 3 is greatest.")
elif a==b==c:
    print("All numbers are equal.")
else:
    print("Enter valid number.")