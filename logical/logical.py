import random
class LogicalMethods:
    
#Gambler game method
    def gamble(self,stake,goal,number_of_time):
        win = 0
        loss = 0
        while number_of_time > 0 :
            if stake == goal :
                print('You won the game...')
                break
            else:
                a = random.random()
                if stake == 0 :
                    print('You lost all the money...')
                    print('$stake = 0 $')
                    break
                elif a > 0.5 :
                    print('won the bet..')
                    stake += 1
                    print('stake =',stake,'$')
                    win += 1
                else :
                    print('loss the bet..')
                    stake -= 1
                    print('stake =',stake,'$')
                    loss += 1
        number_of_time -=1
        number_of_bet = win + loss
        print('Total win : ',win,' Total loss : ' , loss)
        print('win% : ',win*100/number_of_bet)
        print('loss% : ',loss*100/number_of_bet)

#Random unique coupon generator
    #generating random coupon
    def generate(self):
        coupon = random.randrange(100,1000)
        return coupon

    #checking for duplicate values
    def check_duplicate(self,number_of_coupon):
        count = 0
        li = [0 for i in range(number_of_coupon)]
        index = 0
        while index < number_of_coupon:
            count += 1
            duplicate_count = 0
            coupon_number = self.generate()
            for j in range(number_of_coupon):
                if li[j] == coupon_number:
                    duplicate_count += 1
            if duplicate_count > 0 :
                index = index - 1
            else :
                li[index] = coupon_number   
            index += 1
        print('Total random number generated : ',count)
        return li