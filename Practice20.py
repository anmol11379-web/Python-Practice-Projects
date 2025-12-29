# Write a program to find the largest of three numbers using if-elif-else.

a =  int(input("Enter value of a : "))
b =   int(input("Enter value of b : "))
c =   int(input("Enter value of c : "))

if (a>b and a>c):
    print("A is Greatest among a ,b ,c")
elif(b>a and b>c):
    print("B is Greatest among a ,b , c")
elif(c>a and c>b):
    print("C is greatest among a,b,c")
else:
    print("a ,b , c are equal")