from inventoryManager import *

class InvantoryFactory:
    new_manager = InventoryManager()
    while True:
        print('\n1.Display Value \n2.Display inventory items  \n3.display perticular item \n4.Quit')
        try:
            user_input = int(input('Enter your choice : '))
        except ValueError:
            print('Please enter given option')
            continue
        print('------------------INVENTORY---------------------')
        if user_input == 1:
            new_manager.displayInvantoryValue()
        if user_input == 2:
            new_manager.displayAllInventory()
        if user_input == 3:
                element = input('Enter name of item : ')
                new_manager.displayPerticularInventory(element)
        if user_input == 4:
            break
        print('------------------END---------------------')