class UtilDataStructure:
    def read_array(self):
            try:
                array_row = int(input('Enter numbers of row : '))
                array_col = int(input('Enter numbers of rcol : '))
                if array_col < 1 or array_row < 1 :
                    print('length should be more than 0  \ntry again')
                    return self.read_array()
                array = [[0 for i in range(array_col)] for j in range(array_row)]
                array_type = int(input('Enter type of array \n1.String \n2.Int \n3.Float \n'))
            except ValueError:
                print('invalid input!!! \nTry again')
                return self.read_array()
            #for String type 2D array
            if array_type == 1:
                for row in range(array_row):
                    for col in range(array_col):
                        array[row][col] = input('Enter element : ')
            #for integer type 2D array
            elif array_type == 2:
                try:
                    for row in range(array_row):
                        for col in range(array_col):
                            array[row][col] = int(input('Enter element : '))
                except ValueError:
                    print('Invalid input for integer, try again!!!!')
                    return self.read_array()
            #for double type 2D array
            elif array_type == 3:
                try:
                    for row in range(array_row):
                        for col in range(array_col):
                            array[row][col] = float(input('Enter element : '))
                except ValueError:
                    print('Invalid input for float value, try again!!!!')
                    return self.read_array()
            else:
                print('Wrong input ')
                return self.read_array()
            return array

    '''
        - is_prime(number) takes a number as input and will return true if it is prime else 
        it will return false
    '''
    def is_prime(self,num):
            j = 2
            while j <= num//2:
                if num % j == 0:
                    return False
                j += 1
            return True