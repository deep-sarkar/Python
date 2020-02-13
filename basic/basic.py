import random
class Basic :
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

#Power of 2 method
    def table(self,num):
        out_num = 1
        while num >= 2 :
            out_num = out_num * 2
            print(out_num)
            num = num / 2

#Harmonic number generator method
    def harmonicValue(self,count):
        den = 1
        harm_num = 0
        while count > 0 :
            harm_num = harm_num + 1/den
            print(harm_num)
            count -= 1
            den += 1

#Find prime factor of a number
    def primeFactors(self,num):
            while num%2 == 0 :
                print("2")
                num = num/2

            for i in range(3,int(num/2),2):
                while num%i == 0 :
                    print(i)
                    num = num/i
            if num > 1 :
                print(num)