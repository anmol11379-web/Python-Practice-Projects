# Write a recursive fucntion to print all elements in a list 


def list(l,i):
    if i == len(l):
        return 0
    print (l[i])
    list(l,i+1)

l=["a","b","c"]

list(l,0)