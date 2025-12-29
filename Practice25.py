# WAP TO ASK USER IF TODAY IS WEEKEND , CUSTOMER'S AGE , IS TODYA PUBLIC HOLIDAY .
# if today is weekend and age is greater than equal to 65 and no public holiday then print DISCOUND APPLIED ! other wise print NO DISCOUNT TODAY ! 


def gros(d,a,p):

    if day=='Y' and age >=65 and pubholiday=='N':
        print("Discount Applied!")
    elif day=='Y' and age>=65 and pubholiday=='Y':
        print("No Discound Today!") 
    elif day=='Y' and pubholiday=='N':
        print("Discount Applied!")
    elif day=='Y' and pubholiday=='Y':
        print("No Discount Today!")
    else:
        print("No discount!")
    return 

day=input("Is Today Weekend(Saturday or Sunday) ? \n(Y/N) : ")
age=int(input("Enter your age : "))
pubholiday=input("Is today public holiday ? \n(Y/N) : ")
gros(day,age,pubholiday)