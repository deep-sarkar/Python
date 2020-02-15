from algorithm import *
class MergeSort:
    ins = AlgorithmMethods()
    ar = ['Dog','Boy','Apple','Elephant','Cat']
    n = len(ar)
    print('Before sorting : ',ar)
    ins.mergeSort(ar,0,n-1)
    print('After sorting : ',ar)