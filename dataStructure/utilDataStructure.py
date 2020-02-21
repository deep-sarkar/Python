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
    '''
        - allPrime() method to print all prime number in fortm of 2d array
    '''
    def allPrime(self):
        lower_range = 2
        upper_range = 100
        ar =[]
        for i in range(10):
            li = []
            for j in range(lower_range,upper_range):
                if len(li) == 0:
                    li.append(lower_range)
                    li.append(' - ')
                    li.append(upper_range)
                    li.append(' : ')
                if self.is_prime(j):
                    li.append(j)
                if j == upper_range - 1:
                    lower_range = upper_range
                    upper_range += 100
                    ar.append(li)
        return ar
    
    '''
        -to_primeAnagramArray() takes no argument and wil return 2d array 
        - 1st row elements which are prime and not an anagram
        -2nd row elements which are anagram and prime
    '''
    def to_primeAnagramArray(self,lower_range,upper_range):
        anagram_array = ['Anagram array']
        normal_array = ['Normal array']
        array = []
        if lower_range < 2:
            lower_range = 2
        for i in range(lower_range,upper_range):
            if i < 11:
                if self.is_prime(i):
                    normal_array.append(i)
            else:
                if self.is_prime(i):
                    rev = self.reverse_num(i)
                    if self.is_prime(rev):
                        anagram_array.append(i)
                    else:
                        normal_array.append(i)
        array.append(normal_array)
        array.append(anagram_array)
        return array
    '''
        reverse_num(number) will reverse the number and return it
    '''
    def reverse_num(self,num):
        rev = 0
        while num > 0:
            rev = rev*10 + num%10
            num = num//10
        return rev
    
    '''
        - primeAnagram(number) take an integer number as an input and will return if its 
            anagram number is also prime
    '''
    def primeAnagram(self,number):
        if self.is_prime(number):
            rev = self.reverse_num(number)
            if self.is_prime(rev):
                return True
        return False
    '''
        - day_of_week(day,month year) takes 3 argument as input and return day on that day in numerical
            form. ie. 0 = sunday , 6 = saturday
    '''
    def day_of_week(self,day,month,year):
        y1 = year - (14-month)//12
        x = y1 + y1//4 - y1//100 + y1//400
        m1 = month + 12 * ((14-month)//12) - 2
        d1 = (day + x + (31 * m1)//12) % 7
        return d1
    '''
        -is_leapyear(year) method take a year as an input and returns true if year is a leap year
    '''
    def is_leapyear(self,year):
        if year%400 == 0 or year%100 != 0 and year%4 == 0:
            return True
        return False

    
