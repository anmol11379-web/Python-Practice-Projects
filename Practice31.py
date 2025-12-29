# Write a python program to check whether a given number is even or odd. If the
# number is even, print number’s square and if number is odd print number’s cube

def odd_even(x):
    if x%2==0:
        print("Square of the given number is : ", x**2)
    elif x%2!=0:
        print("Cube of the Given number is : ", x**3)

num=int(input("Enter Num1 : "))
odd_even(num)