from algorithm import *
class Permutation:
    per = AlgorithmMethods()
    string = str(input('Enter word : '))
    length = len(string) 
    arr = list(string)
    per.permute(arr,0,length-1)
