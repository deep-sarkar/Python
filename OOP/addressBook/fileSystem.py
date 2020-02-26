import os.path
class FileSystem:
    def __init__(self):
        self.file_name = 'addressBook/address.json'
        
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
                self.file_name = 'addressBook/'+file_name
        except IOError:
            print('File not found')
    
    '''
        -save(self) will save the file
    '''
    def save(self):
        file_name = self.file_name
        new_book = open(file_name,'w+')
        new_book.close()