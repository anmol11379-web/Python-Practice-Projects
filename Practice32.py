# WAP perform sum of cubes of the digits. 

def cube_sum(n):
    sum=0
    while n>0:
        r = n % 10
        sum = sum + r**3
        n = n // 10
    print ("SUM OF CUBE : " , sum)
    return 0
n=int(input("Enter a Number : "))
cube_sum(n)