# Given three list , list1 ,list2,list3 ,
# WAP to add list2  and list3 in list 1 as a single element each .
# the order of list should be list3 , list1 , list2


list1=['a','b','c']
list2=['h','i','t']
list3=['0','1','2']

# # Method-1
# list1.append(list2)
# list1.reverse()
# list1.append(list3)
# print(list1)

# Method-2
list1.append(list2)
list1.insert(0,list3)
print(list1)