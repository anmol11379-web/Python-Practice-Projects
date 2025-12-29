# Write a program to print the Fibonacci sequence up to n terms using a for loop.
# 0 1 1 2 3 5 8 13 ........

n =int(input("Enter no. of terms : "))
a = 0 
b = 1  
print (a)
print (b)

for i in range(1,n-1):
    c=a+b
    print(c)
    a=b 
    b=c

    
