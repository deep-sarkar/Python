import json
from datetime import datetime
from stock import *

my_stock = Stock()
class StockAccount:
    def __init__(self,path):
        self.stockList = {"CompanyShares":[]}
        self.path = path
    
    def valueOf(self):
        my_stock.valueOfAllStock()
    
    def buy(self,amount,stock_name):
        try:
            with open(self.path,'r') as json_file:
                self.stockList = json.load(json_file)
            for stock in self.stockList['CompanyShares']:
                if stock['stock_name'] == stock_name:
                    stock_price = stock['price_per_share']
                    total_stock = stock['number_of_share']
                    new_stock = amount/stock_price
                    total_stock = total_stock + new_stock
                    stock['number_of_share'] = total_stock
                    transaction_time = datetime.now()
                    stock['transaction_time'] = str(transaction_time)
                    self.save()
                    print('Transaction successful')
        except json.decoder.JSONDecodeError:
            print('Stock list is empty')

    def sell(self,amount,stock_name):
        try:
            with open(self.path,'r') as json_file:
                self.stockList = json.load(json_file)
            for stock in self.stockList['CompanyShares']:
                if stock['stock_name'] == stock_name:
                    stock_price = stock['price_per_share']
                    total_stock = stock['number_of_share']
                    new_stock = amount/stock_price
                    total_stock = total_stock - new_stock
                    stock['number_of_share'] = total_stock
                    transaction_time = datetime.now()
                    stock['transaction_time'] = str(transaction_time)
                    self.save()
                    print('Transection successful')
        except json.decoder.JSONDecodeError:
            print('Stock list is empty')
    
    def save(self):
        try:
            with open(self.path,'w') as json_file:
                json.dump(self.stockList,json_file,indent=2)
        except json.decoder.JSONDecodeError:
            print('There is nothing to save !!!')

    def printReport(self):
        my_stock.valueOfEachStock()