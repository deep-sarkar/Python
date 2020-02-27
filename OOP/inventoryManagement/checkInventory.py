from invantoryDataManagement import *

class CheckInventory:
    new_inventory = InventoryDataManagement()
    while True:
        print('\n1.Add data \n2.Display inventory items  \n3.Delete item \n4.Display value \n5.Quit')
        try:
            user_input = int(input('Enter your choice : '))
        except ValueError:
            print('Please enter given option')
            continue
        print('------------------INVENTORY---------------------')
        if user_input == 1:
            new_inventory.addToInventoryData()
        if user_input == 2:
            new_inventory.displayAllInventory()
        if user_input == 3:
            element = input('Enter item name : ')
            new_inventory.deleteItem(element)
        if user_input == 4:
            new_inventory.displayValue()
        if user_input == 5:
            break
        print('--------------------END--------------------')
