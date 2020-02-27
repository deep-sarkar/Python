import json

class InventoryDataManagement:
    def __init__(self):
        self.inventory = {'rice':[],'pulses':[],'wheat':[]}
        self.path = 'inventoryManagement/invantoryData.json'
    
    def add(self):
        flag = True
        goods = {}
        goods['Type'] = input('Enter item name : ')
        while flag:
            try:
                weight = float(input('Enter quantity (weight) : '))
            except ValueError:
                print('Enter weight in correct formate ')
                continue
            goods['Weight'] = weight
            try:
                price_per_kg = float(input('Enter price per kg : '))
            except ValueError:
                print('Enter price in correct formate ')
                continue
            goods['Price_per_kg'] = price_per_kg
            flag = False
        return goods
    
    def addToInventoryData(self,item_type):
        try:
            with open(self.path,'r') as json_file:
                self.inventory = json.load(json_file)
            inventory_data = self.add()
            self.inventory[item_type].append(inventory_data)
        except json.decoder.JSONDecodeError:
            inventory_data = self.add()
            self.inventory[item_type].append(inventory_data)
        with open(self.path,'w') as json_file:
            json.dump(self.inventory,json_file,indent = 2)
    
    def deleteItem(self,item_type,item):
        index = 0
        try:
            with open(self.path,'r') as json_file:
                self.inventory = json.load(json_file)
            for element in self.inventory[item_type]:
                if element['Type'] == item:
                    self.inventory[item_type].pop(index)
                index += 1
        except json.decoder.JSONDecodeError:
            print('Inventory is empty')
        with open(self.path,'w') as json_file:
            json.dump(self.inventory,json_file,indent= 2)
    
    def displayAllInventory(self,item_type):
        try:
            with open(self.path,'r') as json_file:
                self.inventory = json.load(json_file)
            for element in self.inventory[item_type]:
                print('----',element['Type'],'----')
                for item,detail in element.items():
                    print(item,':',detail)
        except json.decoder.JSONDecodeError:
            print('Inventory is empty!!!')

    def displayValue(self,item_type):
        total_value_of_inventory = 0
        try:
            with open(self.path,'r') as json_file:
                self.inventory = json.load(json_file)
            for element in self.inventory[item_type]:
                print('----',element['Type'],'----')
                total_weight = float(element['Weight'])
                value_per_kg = float(element['Price_per_kg'])
                total_value = total_weight*value_per_kg
                total_value_of_inventory += total_value
                print('total_weight :',total_weight)
                print('value_per_kg :',value_per_kg)
                print('Total Value :',total_value)
            print('total value of inventory : ',total_value_of_inventory)
        except json.decoder.JSONDecodeError:
            print('Inventory is empty !!!')
