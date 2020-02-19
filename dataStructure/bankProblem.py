from queue import *
class BankProblem:
    def __init__(self):
        self.balance = 20000
    
    def withdraw(self):
        amount = int(input('Enter amount : '))
        if self.balance > amount :
            self.balance -= amount
            return True
        else :
            print('low balance')
            return self.withdraw()
    
    def deposite(self,amount):
        self.balance = self.balance + amount
        return True
    
q = Queue()
b =BankProblem()
while True:
    print('1.add customer 2.withdraw 3.deposite')
    user_input = int(input('Enter operation : '))
    if user_input == 1:
        name = input('Enter name : ')
        q.enqueue(name)
    elif user_input == 2:
        if b.withdraw():
            print('Transaction successful')
            print(q.dequeue(),' Thankyou')

    elif user_input == 3:
        amount = int(input('Enter amount'))
        b.deposite(amount)
        print('Transaction successful')
        print(q.dequeue(),' Thankyou')


        
