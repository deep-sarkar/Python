from queue import *
from utilDataStructure import *

d = UtilDataStructure()

class AnagramUsingStack:
    s = Queue()
    def addToQueue(cls,lower_range,upper_range):
        low = lower_range
        while low < 2 :
            low += 1
        for i in range(low,upper_range):
            if d.primeAnagram(i):
                cls.s.enqueue(i)
            
            
    def reversePrimeAnagram(cls):
        arr = ['Anagram prime number from higher range to lower range']
        while cls.s.size() != 0:
            num = cls.s.dequeue()
            arr.append(num)
        return arr

an = AnagramUsingStack()
try:
    lower_range = int(input('Enter lower range : '))
    upper_range = int(input('Enter upper range : '))
except ValueError:
    print('Please enter suitable input and try again : ')

an.addToQueue(lower_range,upper_range)
array = an.reversePrimeAnagram()
print(array)
