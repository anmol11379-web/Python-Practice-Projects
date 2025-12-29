# calculate the some of numbers using recursion

def sum(n):
    
    if n<=0:
        return 0
    return sum(n-1)+n
n=int(input("Enter a num :"))
print(sum(n))
