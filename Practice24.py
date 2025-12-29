# Write a program to calculate the factorial of a given number using a while loop.


n = int(input("Enter a number to find factorial: "))
if n < 1:
    print(0)
else:
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    print(factorial)


