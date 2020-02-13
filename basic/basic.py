import random
class Basic:
#check leapyear method 
    def is_leapyear(self,year) :
        if year >= 999 and year <= 9999 :
            n = 2
            if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 :
                print("Leap year")
            else :
                print("Not a leap year")
        else :
            print("Invalid input")
#coin flip method
    def flipCoin(self,toss):
        head = 0
        tail = 0
        while toss > 0 :
            flip = random.random()
            if flip > 0.5 :
                print('Head...')
                head += 1
            else :
                print('Tail...')
                tail += 1
            toss -= 1
        print('head : ',head , ' tail : ',tail)
        total = head + tail
        head_per = "{:.2f}".format(head*100/total)
        tail_per = "{:.2f}".format(tail*100/total)
        print('head% : ' , head_per ,' $ tail% : ', tail_per)