import random
class GamblerGame:
    def __init__(self):
        self.stake = int(input('Enter stake amount : '))
        self.goal = int(input('Enter goal amount : '))
        self.number_of_time = int(input('Enter how many time you want to bet : '))
        self.win = 0
        self.loss = 0

    def gamble(self):
        while self.number_of_time > 0 :
            if self.stake == self.goal :
                print('You won the game...')
                break
            else:
                a = random.random()
                if self.stake == 0 :
                    print('You lost all the money...')
                    print('$stake = 0 $')
                    break
                elif a > 0.5 :
                    print('won the bet..')
                    self.stake += 1
                    print('stake =',self.stake,'$')
                    self.win += 1
                else :
                    print('loss the bet..')
                    self.stake -= 1
                    print('stake =',self.stake,'$')
                    self.loss += 1
            self.number_of_time -=1
gambler = GamblerGame()
gambler.gamble()
number_of_bet = gambler.win + gambler.loss
print('Total win : ',gambler.win,' Total loss : ' , gambler.loss)
print('win% : ',gambler.win*100/number_of_bet)
print('loss% : ',gambler.loss*100/number_of_bet)
