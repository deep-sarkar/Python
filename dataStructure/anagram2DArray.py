from utilDataStructure import *

class Anagram2DArray:
    def execute(self):
        a = UtilDataStructure()
        try:
            lower_range = int(input('Enter lower range : '))
            upper_range = int(input('Upper range : '))
            if lower_range < 0 or upper_range <0:
                print('Please try again and enter integer value greater than 0')
                return self.execute()
            if lower_range < 2:
                while lower_range >= 2:
                    lower_range += 1
            arr = a.to_primeAnagramArray(lower_range,upper_range)
            for row in arr:
                print(row)
        except ValueError:
            print('Please try again and enter integer value in input')
            return self.execute()

an = Anagram2DArray()
an.execute()
    