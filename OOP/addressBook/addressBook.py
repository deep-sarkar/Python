import json
import re
import operator
import os.path
import person

class AddressBook(person.Person):
    def __init__(self):
        self.address_book = {"people" : []}
        self.path = 'addressBook/address.json'

    '''
        -addToJson(self) method internally calling addNew(self) method and saving detail in opened
            file
    '''
    def addToJson(self):
        try:
            with open(self.path,'r') as json_file:
                self.address_book = json.load(json_file)
            detail = self.addNew()
            self.address_book['people'].append(detail)
        except json.decoder.JSONDecodeError:
            detail = self.addNew()
            self.address_book['people'].append(detail)
        with open(self.path,'w') as json_file:
            json.dump(self.address_book,json_file,indent=2)

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
    
    '''
        -delete(self,first_name) method taking first_name and Last_name as an argument and will delete perticular name
            contact
    '''
    def delete(self,first_name,Last_name):
        index = 0
        try:
            with open(self.path,'r') as json_file:
                self.address_book = json.load(json_file)
            for element in self.address_book['people']:
                if element['First_name'] == first_name and element['Last_name']:
                    print(element)
                    self.address_book['people'].pop(index)
                index += 1
        except json.decoder.JSONDecodeError:
            print('Book is empty')
        with open(self.path,'w') as json_file:
            json.dump(self.address_book,json_file,indent=2)

    '''
        -displayContactName(self) method will display all saved contacts first name
    '''
    def displayContactName(self):
        count = 1
        try:
            with open(self.path,'r') as json_file:
                self.address_book = json.load(json_file)
            for element in self.address_book['people']:
                print(count,'.',element['First_name'])
                count += 1
        except json.decoder.JSONDecodeError:
            print('Book is empty')      

    '''
        -displayContactDetail(self,name) take name as input and will display all details the details
            of perticular contact
    '''
    def displayContactDetail(self,name):  
        try:
            with open('address.json','r') as json_file:
                self.address_book = json.load(json_file)
            for element in self.address_book['people']:
                if element['First_name'] == name:
                    print(element['First_name'])
                    for contact,detail in element.items():
                        print(contact,':',detail)
        except json.decoder.JSONDecodeError:
            print('Book is empty')      

    '''
        -editContact(self,name) method is taking 1 argument as name and if contact is there
            it will allow to modify it
    '''
    def editContact(self,name):
        try:
            with open(self.path,'r') as json_file:
                    self.address_book = json.load(json_file)
            for element in self.address_book['people']:
                if element['First_name'] != name:
                    continue
                else :
                    print('what you want to modify !!!')
                    print('\n1.First Name \n2.Last Name \3.Mobile Number \n4.Address \n5.city \n6.State \n7.Zip Code')
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
                        element['address'] = input('address : ')
                    if user_input == 5:
                        detail['city'] = input('city : ')
                    if user_input == 6:
                        detail['state'] = input('state : ')
                    if user_input == 7:
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
    
    '''
        -sortByZIP(self) method will display contacts by sortin them according to zip code
    '''
    def sortByZIP(self):
        count = 1
        try:
            with open(self.path,'r') as json_file:
                self.address_book = json.load(json_file)
                self.address_book['people'].sort(key=operator.itemgetter('zip_code'))
            for element in self.address_book['people']:
                print(count,'.',element['First_name'])
                count += 1
        except json.decoder.JSONDecodeError:
            print('Book is empty')  

    '''
        -sortByName(self) will sort all the contacts according to first name
    '''
    def sortByName(self):
        count = 1
        try:
            with open(self.path,'r') as json_file:
                self.address_book = json.load(json_file)
                self.address_book['people'].sort(key=operator.itemgetter('First_name'))
            for element in self.address_book['people']:
                print(count,'.',element['First_name'])
                count += 1
        except json.decoder.JSONDecodeError:
            print('Book is empty')  
    
    '''
        displayAll(self) method will show all the contact present in the opened book
    '''
    def displayAll(self):
        try:
            with open(self.path,'r') as json_file:
                self.address_book = json.load(json_file)
            for element in self.address_book['people']:
                print('----',element['First_name'],'----')
                for people,detail in element.items():
                    print(people,':',detail)
                print()
        except json.decoder.JSONDecodeError:
            print('Book is empty')      


