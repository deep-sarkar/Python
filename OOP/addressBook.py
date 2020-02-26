import json
import re
class AddressBook:
    def __init__(self):
        self.address_book = {"contact" : []}
        
    def addNew(self):
        flag = True
        flag1 = True
        detail = {}
        detail['First_name'] = input('name : ')
        detail['Last_name'] = input('Last name : ')
        try:
            with open('address.json','r') as json_file:
                data = json.load(json_file)
            for person in data['contact']:
                if detail['First_name'] == person['First_name'] and detail['Last_name'] == person['Last_name']:
                    print('Contact already exist, please try again')
                    return self.addNew()
        except json.decoder.JSONDecodeError:
            print('Adding 1st contact')
        while flag:
            mobile_number = input('mobile_number : ')
            regex = '[6789]{1}[0-9]{9}'
            if re.search(regex,mobile_number) :
                flag = False
                detail['Mobile_no'] = int(mobile_number)
            else :
                print('Invalid mobile number, please enter again')
        detail['state'] = input('state : ')
        while flag1:
            zip_code = input('ZIP code : ')
            regex = '[0-9]{6}'
            if re.search(regex,zip_code) :
                flag1 = False
                detail['zip_code'] = int(zip_code)
            else :
                print('Invalid zip code, please enter again')
        return detail

    def addToJson(self):
        try:
            with open('address.json','r') as json_file:
                self.address_book = json.load(json_file)
            detail = a.addNew()
            self.address_book['contact'].append(detail)
        except json.decoder.JSONDecodeError:
            detail = a.addNew()
            self.address_book['contact'].append(detail)
        with open('address.json','w') as json_file:
            json.dump(self.address_book,json_file,indent=2)
       
    def delete(self,name):
        index = 0
        try:
            with open('address.json','r') as json_file:
                self.address_book = json.load(json_file)
            for element in self.address_book['contact']:
                if element['First_name'] == name:
                    print(element)
                    self.address_book['contact'].pop(index)
                index += 1
        except json.decoder.JSONDecodeError:
            print('Book is empty')
        with open('address.json','w') as json_file:
            json.dump(self.address_book,json_file,indent=2)

    def displayContactName(self):
        count = 1
        try:
            with open('address.json','r') as json_file:
                self.address_book = json.load(json_file)
            for element in self.address_book['contact']:
                print(count,'.',element['First_name'])
                count += 1
        except json.decoder.JSONDecodeError:
            print('Book is empty')        


a = AddressBook()
while True:
    print('\n1.add \n2.delete \n3.display all contact by name')
    user_input = int(input('eneter your choice : '))
    if user_input == 1:
        a.addToJson()
    if user_input == 2:
        name = input('Enter first name : ')
        a.delete(name)
    if user_input == 3:
        a.displayContactName()


# while True:
#     exit = input('Do you want to see detaily y/n ?')
#     if exit.lower() == 'n':
#         break
#     else:
#         try:
#             serial_num = int(input('Enter first serial_num : '))
#             serial_num = str(serial_num)
#         except ValueError:
#             print('Key must be a numerical value')
#             continue
#         try:
#             with open('address.json','r') as file:
#                 data = json.load(file)
#             if serial_num in data.keys():
#                 print('yes')
#             for d, d1 in data[serial_num].items():
#                 print(d,"--->", d1)
#         except KeyError:
#             print('invalid serial number')