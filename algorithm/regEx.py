import re
class RegEx:
    def validate_name(self,name):
        regex = '[A-Z]{1}[a-z]+[w ]+[A-Z]{1}[a-z]'
        if re.search(regex,name) :
            print('Valid name')
        else :
            print('Invalid name')
    
    def validate_ph_number(self,ph_number):
        regex = '[6789]{1}[0-9]{9}'
        if re.search(regex,ph_number) :
            print('Valid mobile number')
        else :
            print('Invalid nmobile number')
    
    def validate_email(self,email):
        regex = '[a-zA-Z0-9]+@[a-z]+\.[a-z]'
        if re.C(regex,email) :
            print('Valid email')
        else :
            print('Invalid email')

ob = RegEx()
name = 'Deep Sarkar'
ob.validate_name(name)
phno = '7023536113'
ob.validate_ph_number(phno)
email = 'deepsarkar96@gmail.com'
ob.validate_email(email)