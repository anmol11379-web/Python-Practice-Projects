
# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)

lst=['a','b','c','b','a']
print("original list ",lst)
copy_lst=lst.copy()
copy_lst.reverse()
if lst==copy_lst:
    print("palindrome")
else:
    print("not palindrome")





# my_list = ['r', 'a', 'c', 'e', 'c', 'a', 'a']

# if my_list == my_list[::-1]:
#     print("The list is a palindrome.")
# else:
#     print("The list is not a palindrome.")