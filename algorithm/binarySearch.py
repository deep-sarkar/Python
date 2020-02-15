from algorithm import *
class BinarySearch:
    b = AlgorithmMethods()
    array = ['Apple','Boy','Cat','Dog','Elephant']
    print(array)
    length = len(array)
    word = str(input('Enter word : '))
    index = b.binSearch(array, 0, length, word)
    print('Your element is present at :',index)

    