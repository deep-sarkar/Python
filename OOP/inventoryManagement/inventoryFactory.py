from inventoryManager import *
from checkInventory import *

class InvantoryFactory:
    new_manager = InventoryManager()
    my_inventory = CheckInventory()
    while True:
        print('\n1.Display Value \n2.Display inventory items  \n3.display perticular item \n4.Quit')
        try:
            user_input = int(input('Enter your choice : '))
        except ValueError:
            print('Please enter given option')
            continue
        print('------------------INVENTORY---------------------')
        if user_input == 1:
            item_type = my_inventory.invantoryType()
            new_manager.displayInvantoryValue(item_type)
        if user_input == 2:
            item_type = my_inventory.invantoryType()
            new_manager.displayAllInventory(item_type)
        if user_input == 3:
            item_type = my_inventory.invantoryType()
            element = input('Enter name of item : ')
            new_manager.displayPerticularInventory(item_type, element)
        if user_input == 4:
            break
        print('------------------END---------------------')