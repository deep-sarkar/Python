from stockAccount import *
class ManageStock:
    my_account = StockAccount('stock/stockData.json')
    while True:
        print('\n1.Buy \n2.Sell \n3.Display each stock value \n4.Total account value \n5.quit')
        try:
            user_input = int(input('Enter your choice : '))
        except ValueError:
            print('Choose right option!!!')

        print('--------------------STACK REPORT------------------------')
        if user_input == 1:
            stock_name = input('Enter stock name : ')
            amount = float(input('Enter amount : '))
            my_account.buy(amount,stock_name)
        if user_input == 2:
            stock_name = input('Enter stock name : ')
            amount = float(input('Enter amount : '))
            my_account.sell(amount,stock_name)
        if user_input == 3:
            my_account.printReport()
        if user_input == 4:
            my_account.valueOf()
        if user_input == 5:
            break
        print('-------------------END------------------------------')