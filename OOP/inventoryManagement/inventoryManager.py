from invantoryDataManagement import *
import json

new_inventory = InventoryDataManagement()
class InventoryManager:
    def __init__(self):
        self.inventory = {'details' : []}
        self.path = 'inventoryManagement/invantoryData.json'
    
    def displayPerticularInventory(self,item):
        try:
            with open(self.path,'r') as json_file:
                self.inventory = json.load(json_file)
            for element in self.inventory['details']:
                if element['Type'] == item:
                    for item, detail in element.items():
                        print(item,':',detail)
        except json.decoder.JSONDecodeError:
            print('Inventory is empty!!!')
    
    def displayAllInventory(self):
        new_inventory.displayAllInventory()
        
    def displayInvantoryValue(self):
        new_inventory.displayValue()