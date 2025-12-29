#calculate the some of first n natural numebrs 

def naturalsum(n):
    if (n == n+1 or n == 0) :
        return 0
    return naturalsum(n-1) + n

print(naturalsum(6))