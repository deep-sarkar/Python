from addressBook import *
class userAddressBook:
    new_addressBook = AddressBook()
    flag = True
    while flag:
        print('''\n1.add \n2.delete \n3.display all name \n4.display detail \n5.edit \n6.Sort by Zip
        \n7.Sort by name \n8.Quit''')
        try:
            user_input = int(input('eneter your choice : '))
        except ValueError :
            print('Try again')
            flag = True
        if user_input == 1:
            new_addressBook.addToJson()
        if user_input == 2:
            name = input('Enter first name : ')
            new_addressBook.delete(name)
        if user_input == 3:
            new_addressBook.displayContactName()
        if user_input == 4:
            name = input('Enter 1st name : ')
            new_addressBook.displayContactDetail(name)
        if user_input == 5:
            name = input('Enter 1st name : ')
            new_addressBook.editContact(name)
        if user_input == 6:
            new_addressBook.sortByZIP()
        if user_input == 7:
            new_addressBook.sortByName()
        if user_input == 8:
            flag = False

