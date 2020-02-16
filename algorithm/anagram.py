from algorithm import *
class AnagramDetection:
    al = AlgorithmMethods()
    string1 = input('Enter 1st line : ')
    string2 = input('Enter 2nd line : ')
    if al.is_anagram(string1,string2):
        print('Anagram')
    else:
        print('Not an anagrams')