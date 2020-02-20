from stack import *
from utilDataStructure import *

d = UtilDataStructure()

class AnagramUsingStack:
    s = Stack()
    count = 0
    def addToStack(cls,lower_range,upper_range):
        low = lower_range
        while low < 2 :
            low += 1
        for i in range(low,upper_range):
            if d.primeAnagram(i):
                cls.s.push(i)
                cls.count += 1
            
    def reversePrimeAnagram(cls):
        arr = ['Anagram prime number from higher range to lower range']
        while cls.count != 0:
            num = cls.s.pop()
            arr.append(num)
            cls.count -= 1
        return arr

an = AnagramUsingStack()
try:
    lower_range = int(input('Enter lower range : '))
    upper_range = int(input('Enter upper range : '))
except ValueError:
    print('Please enter suitable input and try again : ')

an.addToStack(lower_range,upper_range)
array = an.reversePrimeAnagram()
print(array)
