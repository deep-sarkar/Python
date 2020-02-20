from utilDataStructure import *

p = UtilDataStructure()

class Prime2DArray:
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
                if p.is_prime(j):
                    li.append(j)
                if j == upper_range - 1:
                    lower_range = upper_range
                    upper_range += 100
                    ar.append(li)
        return ar


c = Prime2DArray()
array = c.allPrime()
for row in array:
    print(row)            