from logical import *
class GamblerGame:
    stake = int(input('Enter stake amount : '))
    goal = int(input('Enter goal amount : '))
    number_of_time = int(input('Enter how many time you want to bet : '))
    gambler = LogicalMethods()
    
    #Passing argument for gambler method
    gambler.gamble(stake,goal,number_of_time)
    
