# Write a function to check if a number is prime.

def is_prime(num):
    if num <= 1:
        print("Number should be Greater than 1!")
        return 0
    elif num == 2:
        print("Prime Number.")
        return 0
    for i in range(2, num + 1):
        if num % i == 0:
            print("Not a Prime number.")
            break
        elif num % i != 0:
            print("Prime Number.")
            break
num=int(input("Enter a number : "))
is_prime(num)