from invantoryDataManagement import *
import json

new_inventory = InventoryDataManagement()
class InventoryManager:
    def __init__(self):
        self.inventory = {'rice':[],'pulses':[],'wheat':[]}
        self.path = 'inventoryManagement/invantoryData.json'
    
    def displayPerticularInventory(self,item_type,item):
        try:
            with open(self.path,'r') as json_file:
                self.inventory = json.load(json_file)
            for element in self.inventory[item_type]:
                if element['Type'] == item:
                    for item, detail in element.items():
                        print(item,':',detail)
        except json.decoder.JSONDecodeError:
            print('Inventory is empty!!!')
    
    def displayAllInventory(self,item_type):
        new_inventory.displayAllInventory(item_type)
        
    def displayInvantoryValue(self,item_type):
        new_inventory.displayValue(item_type)