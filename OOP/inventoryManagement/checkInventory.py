from invantoryDataManagement import *

class CheckInventory:
    def invantoryType(self):
        print('\n1.Rice \n2.Pulses \n3.Wheat')
        try:
            choice = int(input('Enter item type : '))
        except ValueError:
            print('Please enter right option')
            return self.invantoryType()
        if choice == 1:
            item_type = 'rice'
        if choice == 2:
            item_type = 'pulses'
        if choice == 3:
            item_type = 'wheat'
        return item_type

if __name__ == "__main__":
    new_inventory = InventoryDataManagement()
    my_inventory = CheckInventory()
    while True:
        print('\n1.Add data \n2.Display inventory items  \n3.Delete item \n4.Display value \n5.Quit')
        try:
            user_input = int(input('Enter your choice : '))
        except ValueError:
            print('Please enter given option')
            continue
        print('------------------INVENTORY---------------------')
        if user_input == 1:
            item_type = my_inventory.invantoryType()
            new_inventory.addToInventoryData(item_type)
        if user_input == 2:
            item_type = my_inventory.invantoryType()
            new_inventory.displayAllInventory(item_type)
        if user_input == 3:
            item_type = my_inventory.invantoryType()
            element = input('Enter item name : ')
            new_inventory.deleteItem(item_type, element)
        if user_input == 4:
            item_type = my_inventory.invantoryType()
            new_inventory.displayValue(item_type)
        if user_input == 5:
            break
        print('--------------------END--------------------')
