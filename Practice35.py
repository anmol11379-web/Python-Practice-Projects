

lst_add = []

choice = int(input("Press 1 to book a seat : \nPress 2 to cancel a reservation : \nPress 3 to View the current reservation status : "))

if choice == 1:
    while True:
        ch = input("Do you want to book a seat? (y/n): ").lower()
        if ch == 'y':
            name = input("Enter Name to book a seat : ")
            lst_add.append(name)
            print("Booked a Seat successfully!", lst_add)
        elif ch == 'n':
            print("Thanks for booking!")
            break
        else:
            print("Invalid Entry!")
            break

elif choice == 2:
    while True:
        cncl = input("Enter Name of Passenger to cancel seat : ")
        if cncl in lst_add:
            lst_add.remove(cncl)
            print("Canceled the reservation successfully!", lst_add)
        else:
            print("No Reservation found with the given name!")
        
        ph = input("Do you want to cancel more seats? (y/n): ").lower()
        if ph == 'y':
            continue
        elif ph == 'n':
            print("Have a Nice day!")
            break
        else:
            print("Invalid Entry!")
            break

elif choice == 3:
    print("Current Status of Reservations : ", lst_add)

else:
    print("Invalid entry.")
