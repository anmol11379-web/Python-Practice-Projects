# Write a program to reverse a string using a loop.

# s="STRING"
# newstr=""
# for i in s:
#     newstr=i+newstr
# print("Reversed String : ",newstr)


def reverse(s):
    newstr=""
    for i in s:
        newstr=i+newstr
    print("Reversed String : ",newstr)
    return 0

s=str(input("Enter a String : "))
print("Original String : ",s)
reverse(s)

 