from deque import *
class Palindrom:
    def is_palindrom(self,item):
        d = Deque()
        for i in item:
                d.addFront(i)
        while d.size() > 1:
            condition_1 = d.removeFront()
            condition_2 = d.removeRear()
            if condition_1 != condition_2:
                return False
        return True

p = Palindrom()
user_input = input('Enter your word : ')
check = p.is_palindrom(user_input)
if check:
    print('Its a palindrom')
else :
    print('Its not apalindrom')