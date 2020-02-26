import json
import re
import operator
import os.path

class AddressBook:
    def __init__(self):
        self.address_book = {"contact" : []}
        self.path = 'addressBook/address.json'

    '''
        -create(self) when method will called, it will create a new file.
    '''
    def create(self):
        try:
            file_name = input('Enter file name : ')
            file_name = file_name+'.json'
            if os.path.isfile(file_name):
                print ("File exist")
                return self.create()
            else :
                file_name1 = 'addressBook/'+file_name
                new_book = open(file_name1,'w+')
                new_book.close()
        except IOError:
            print('File not found')
    
    '''
        -open(self) method will open an existing file from directory
    '''
    def open(self):
        file_name = input('Enter file name : ')
        file_name = file_name+'.json'
        try:
            file_name1 = 'addressBook/'+file_name
            with open(file_name1) as my_file:
                self.address_book = json.load(my_file)
            self.path = file_name1
            print(self.path)
        except IOError:
            print('File not found')
        except json.decoder.JSONDecodeError:
            print('New file opened')
            self.path = file_name1
            print(self.path)
    

    def addNew(self):
        flag = True
        flag1 = True
        detail = {}
        detail['First_name'] = input('name : ')
        detail['Last_name'] = input('Last name : ')
        try:
            with open(self.path,'r') as json_file:
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
        detail['city'] = input('city : ')
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
            with open(self.path,'r') as json_file:
                self.address_book = json.load(json_file)
            detail = self.addNew()
            self.address_book['contact'].append(detail)
        except json.decoder.JSONDecodeError:
            detail = self.addNew()
            self.address_book['contact'].append(detail)
        with open(self.path,'w') as json_file:
            json.dump(self.address_book,json_file,indent=2)
       
    def delete(self,name):
        index = 0
        try:
            with open(self.path,'r') as json_file:
                self.address_book = json.load(json_file)
            for element in self.address_book['contact']:
                if element['First_name'] == name:
                    print(element)
                    self.address_book['contact'].pop(index)
                index += 1
        except json.decoder.JSONDecodeError:
            print('Book is empty')
        with open(self.path,'w') as json_file:
            json.dump(self.address_book,json_file,indent=2)

    def displayContactName(self):
        count = 1
        try:
            with open(self.path,'r') as json_file:
                self.address_book = json.load(json_file)
            for element in self.address_book['contact']:
                print(count,'.',element['First_name'])
                count += 1
        except json.decoder.JSONDecodeError:
            print('Book is empty')      

    def displayContactDetail(self,name):  
        try:
            with open('address.json','r') as json_file:
                self.address_book = json.load(json_file)
            for element in self.address_book['contact']:
                if element['First_name'] == name:
                    print(element['First_name'])
                    for contact,detail in element.items():
                        print(contact,':',detail)
        except json.decoder.JSONDecodeError:
            print('Book is empty')      

    def editContact(self,name):
        try:
            with open(self.path,'r') as json_file:
                    self.address_book = json.load(json_file)
            for element in self.address_book['contact']:
                if element['First_name'] != name:
                    continue
                else :
                    print('what you want to modify !!!')
                    print('\n1.First Name \n2.Last Name \3.Mobile Number \n4.State \n5.Zip Code')
                    try:
                        user_input = int(input('Enter your choice : '))
                        if 0 > user_input > 6:
                            print('Please enter correct value !!!')
                            self.editContact(name)
                    except ValueError:
                        print('Please enter right input and try again')
                        self.editContact(name)
                    if user_input == 1:
                        element['First_name'] = input('name : ')
                    if user_input == 2:
                        element['Last_name'] = input('Last name : ')
                    if user_input == 3:
                        flag = True
                        while flag:
                            mobile_number = input('mobile_number : ')
                            regex = '[6789]{1}[0-9]{9}'
                            if re.search(regex,mobile_number) :
                                flag = False
                                element['Mobile_no'] = int(mobile_number)
                            else :
                                print('Invalid mobile number, please enter again')
                    if user_input == 4:
                        element['state'] = input('state : ')
                    if user_input == 5:
                        flag1 = True
                        while flag1:
                            zip_code = input('ZIP code : ')
                            regex = '[0-9]{6}'
                            if re.search(regex,zip_code) :
                                flag1 = False
                                element['zip_code'] = int(zip_code)
                            else :
                                print('Invalid zip code, please enter again')
        except json.decoder.JSONDecodeError:
            print('Book is empty')      
        with open(self.path,'w') as json_file:
            json.dump(self.address_book,json_file,indent=2)
    
    def sortByZIP(self):
        count = 1
        try:
            with open(self.path,'r') as json_file:
                self.address_book = json.load(json_file)
                self.address_book['contact'].sort(key=operator.itemgetter('zip_code'))
            for element in self.address_book['contact']:
                print(count,'.',element['First_name'])
                count += 1
        except json.decoder.JSONDecodeError:
            print('Book is empty')  

    def sortByName(self):
        count = 1
        try:
            with open(self.path,'r') as json_file:
                self.address_book = json.load(json_file)
                self.address_book['contact'].sort(key=operator.itemgetter('First_name'))
            for element in self.address_book['contact']:
                print(count,'.',element['First_name'])
                count += 1
        except json.decoder.JSONDecodeError:
            print('Book is empty')  
    
    def displayAll(self):
        try:
            with open('address.json','r') as json_file:
                self.address_book = json.load(json_file)
            for element in self.address_book['contact']:
                if element['First_name'] == name:
                    print(element['First_name'])
                    for contact,detail in element.items():
                        print(contact,':',detail)
        except json.decoder.JSONDecodeError:
            print('Book is empty')      


