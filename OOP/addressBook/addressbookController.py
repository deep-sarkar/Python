from addressBook import *
from fileSystem import *
import fnmatch
class userAddressBook:

    print('-------------------------- My AddressBook ----------------------------')
    all_books = fnmatch.filter(os.listdir('addressBook'), '*.json')
    total_books = len(all_books)
    print("total saved book : ",total_books)
    book_count = 1
    for book in all_books:
        print(book_count,'.',book)
        book_count += 1
    print('------------------------------------------------------------------',end='')
    new_addressBook = AddressBook()
    while True:
        print('\n1.Open existing book \n2.Create new book \n3.Quit')
        try:
            user_input = int(input('Enter your choice : '))
        except ValueError:
            print('Please enter right option')
            continue
        if user_input == 1:
            new_addressBook.open()
            while True:
                print('''\n1.add \n2.delete \n3.display all name \n4.display detail \n5.edit \n6.Sort by Zip \n7.Sort by name \n8.Display all contacts \n9.Quit''')
                try:
                    user_input = int(input('eneter your choice : '))
                except ValueError :
                    print('Try again')
                    continue
                if user_input == 1:
                    new_addressBook.addToJson()
                if user_input == 2:
                    first_name = input('Enter first name : ')
                    last_name = input('Enter last name : ')
                    new_addressBook.delete(first_name,last_name)
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
                    new_addressBook.displayAll()
                if user_input == 9:
                    break
                print('***********************************************',end='')
        if user_input == 2:
            new_file = FileSystem()
            new_file.create()
            my_file = input('To save file print y')
            if my_file == 'y' or my_file == 'Y':
                new_file.save()
                print('File saved')
        print('------------------------------------------------------------------',end='')
        if user_input == 3:
            break

