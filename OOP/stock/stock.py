import json
from datetime import datetime

class Stock:
    def __init__(self):
        self.stockList = {"CompanyShares":[]}
        self.path = "stock/stockData.json"
    
    def addStock(self):
        try:
            stock_name = input('Enter stock name : ')
            number_of_share = float(input('enter number of share : '))
            price_per_share = float(input('Enter price per share : '))
        except ValueError:
            print('Please enter correct data and try again !!!')
        except TypeError:
            print('Please enter correct data and try again !!!')
        stock_detail = {}
        stock_detail['stock_name'] = stock_name
        stock_detail['number_of_share'] = number_of_share
        stock_detail['price_per_share'] = price_per_share
        transaction_time = datetime.now()
        stock_detail['transaction_time'] = str(transaction_time)
        try:
            with open(self.path,'r') as json_file:
                self.stockList = json.load(json_file)
            self.stockList['CompanyShares'].append(stock_detail)
        except json.decoder.JSONDecodeError:
            print('Adding 1st stock detail')
            self.stockList['CompanyShares'].append(stock_detail)
        with open(self.path,'w') as json_file:
            json.dump(self.stockList,json_file,indent=2)
            
    def valueOfEachStock(self):
        try:
            with open(self.path,'r') as json_file:
                self.stockList = json.load(json_file)
            for stock in self.stockList["CompanyShares"]:
                print('----',stock['stock_name'],'----')
                number_of_share = stock['number_of_share']
                price_per_stock = stock['price_per_share']
                total_price = number_of_share*price_per_stock
                print('Total price : ',total_price)
        except json.decoder.JSONDecodeError:
            print('Stock file is empty')
    
    def valueOfAllStock(self):
        price_of_all_stock = 0
        try:
            with open(self.path,'r') as json_file:
                self.stockList = json.load(json_file)
            for stock in self.stockList['CompanyShares']:
                number_of_share = stock['number_of_share']
                price_per_stock = stock['price_per_share']
                total_price = number_of_share*price_per_stock
                price_of_all_stock += total_price
            print('Price of all stock :',price_of_all_stock)
        except json.decoder.JSONDecodeError:
            print('You have no stocks!!!')
