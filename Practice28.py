# Write a recursive function to compute the factorial of a number.

def fact(n):
    factorial=1
    for i in range(1,n+1):
        factorial *= i
    
    return factorial

n=int(input("Enter a number to find factorial : "))
print(fact(n))


# def fact(n):
#     factorial=1
    
#     for i in range (1,n+1):
#         while (1> n):
#             return 0
#         factorial *= i
#     return factorial

# n=int(input("Enter a number to find factorial : "))
# print(fact(n))
