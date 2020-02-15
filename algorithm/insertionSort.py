from algorithm import *
class InsertionSort:
    ins = AlgorithmMethods()
    ar = [7,2,9,5,9,1,7,6,4]
    print('Before sorting : ',ar)
    ins.insertion_sort(ar)
    print('After sorting : ',ar)