import json
import re
class AddressBook:
        
    def addNew(self):
        flag = True
        detail = {}
        detail['First_name'] = input('name : ')
        detail['Last_name'] = input('Last name : ')
        while flag:
            mobile_number = input('mobile_number : ')
            regex = '[6789]{1}[0-9]{9}'
            if re.search(regex,mobile_number) :
                flag = False
                detail['Mobile_no'] = int(mobile_number)
            else :
                print('Invalid nmobile number, please enter again')
        detail['state'] = input('state : ')
        return detail

a = AddressBook()
address_book = {"contact" : []}

while True:
    exit = input('Do you want to add y/n ?')
    if exit.lower() == 'n':
        break
    else:
        try:
            with open('address.json','r') as f:
                address_book = json.load(f)
            detail = a.addNew()
            address_book['contact'].append(detail)
        except json.decoder.JSONDecodeError:
            detail = a.addNew()
            address_book['contact'].append(detail)
    with open('address.json','w') as json_file:
        json.dump(address_book,json_file,indent=2)

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