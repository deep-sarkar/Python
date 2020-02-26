from invantoryDataManagement import *
class CheckInventory:
    new_inventory = InventoryDataManagement()

    while True:
        print('\n1.Add data \n2.Display inventory items \n3.display perticular item detail \n4.Delete item \n5.Display value \n6.Quit')
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
            element = input('Enter name of item : ')
            new_inventory.displayPerticularInventory(element)
        if user_input == 4:
            element = input('Enter item name : ')
            new_inventory.deleteItem(element)
        if user_input == 5:
            new_inventory.displayValue()
        if user_input == 6:
            break
        print('--------------------END--------------------')
