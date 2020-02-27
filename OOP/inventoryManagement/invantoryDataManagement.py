import json

class InventoryDataManagement:
    def __init__(self):
        self.inventory = {'details' : []}
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
    
    def addToInventoryData(self):
        try:
            with open(self.path,'r') as json_file:
                self.inventory = json.load(json_file)
            inventory_data = self.add()
            self.inventory['details'].append(inventory_data)
        except json.decoder.JSONDecodeError:
            inventory_data = self.add()
            self.inventory['details'].append(inventory_data)
        with open(self.path,'w') as json_file:
            json.dump(self.inventory,json_file,indent = 2)
    
    def displayAllInventory(self):
        try:
            with open(self.path,'r') as json_file:
                self.inventory = json.load(json_file)
            for element in self.inventory['details']:
                print('----',element['Type'],'----')
                for item,detail in element.items():
                    print(item,':',detail)
        except json.decoder.JSONDecodeError:
            print('Inventory is empty!!!')
    
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
    
    def deleteItem(self,item):
        index = 0
        try:
            with open(self.path,'r') as json_file:
                self.inventory = json.load(json_file)
            for element in self.inventory['details']:
                if element['Type'] == item:
                    self.inventory['details'].pop(index)
                index += 1
        except json.decoder.JSONDecodeError:
            print('Inventory is empty')
        with open(self.path,'w') as json_file:
            json.dump(self.inventory,json_file,indent= 2)
    
    def displayValue(self):
        try:
            with open(self.path,'r') as json_file:
                self.inventory = json.load(json_file)
            for element in self.inventory['details']:
                print('----',element['Type'],'----')
                total_weight = float(element['Weight'])
                value_per_kg = float(element['Price_per_kg'])
                print('total_weight :',total_weight)
                print('value_per_kg :',value_per_kg)
                print('Total Value :',total_weight*value_per_kg)
        except json.decoder.JSONDecodeError:
            print('Inventory is empty !!!')
