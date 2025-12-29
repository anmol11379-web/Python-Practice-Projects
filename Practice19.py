# Write a program to swap the values of two variables without using a third variable.


# def swap(x,y):
#     x,y=y,x
#     return x,y
# a=int(input("Enter the value of a :"))
# b=int(input("Enter the value of b :"))
# new=swap(a,b)
# print("Before sawp")
# print("a = " , a)
# print("b = " , b )
# print("After sawp")
# print("a , b = " , new) 

# ============ METHOD 2 ===============

x = 5
y=10
print("Before sawp")
print("x = " , x)
print("y = " , y )
x=x+y
y=x-y
x=x-y
print("After sawp")
print("x = ",  x)
print("y = " , y) 

