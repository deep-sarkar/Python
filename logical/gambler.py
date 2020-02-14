from logical import *
class GamblerGame:
    gambler = LogicalMethods()
    gambler.gamble()
    number_of_bet = gambler.win + gambler.loss
    print('Total win : ',gambler.win,' Total loss : ' , gambler.loss)
    print('win% : ',gambler.win*100/number_of_bet)
    print('loss% : ',gambler.loss*100/number_of_bet)
