student_list = input("Enter data to store: ").split()

while True:
    ch = input("Do you want to add more data? (Y/N): ")
    if ch == 'Y' or ch == 'y':
        add_data = input("Enter data to store: ").split()
        student_list.extend(add_data)  
    elif ch == 'N' or ch == 'n':
        print("Data successfully added!", student_list)
        break
    else:
        print("Invalid choice! Enter Y or N.")
    out = input("Do you want to remove any info? (Y/N): ")
    if out == 'Y' or out == 'y':
        name = input("Enter Name you want to remove: ")
        if name in student_list:
            student_list.remove(name)  
        else:
            print("Given Name is not in DataBase!")

    elif out == 'N' or out == 'n':
        print("Data successfully updated!\n Final Updated List : ",  student_list)
    else:
        print("Invalid entry!")

    
