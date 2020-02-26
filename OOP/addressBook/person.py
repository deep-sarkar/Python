import json
import re
class Person:
    def __init__(self):
        self.address_book = {"contact" : []}
        self.path = 'addressBook/address.json'

    '''
        -addNew(self) method woll collect all information from user and return it in 
            the form of dictionary object
    '''
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

    '''
        -addToJson(self) method internally calling addNew(self) method and saving detail in opened
            file
    '''
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