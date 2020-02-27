from stock import *
class StockPortFolio:
    new_stock = Stock()
    while True:
        
        print('\n1.Add stock \n2.Display value of each stock \n3.Display value of all stock \n4.Quit')
        try:
            user_input = int(input('Enter your choice : '))
        except ValueError:
            print('Please enter a correct value and try again')
        print('--------------------Stock Report------------------------')
        if user_input == 1:
            new_stock.addStock()
        if user_input == 2:
            new_stock.valueOfEachStock()
        if user_input == 3:
            new_stock.valueOfAllStock()
        if user_input == 4:
            break
        print('---------------------END-------------------------')