from stack import Stack
class BalanceParentheses:
    '''
        -Function to check parentheses are properly balanced or not
    '''
    def is_balanced(self,user_input): 
        if len(user_input)%2 != 0:
            return "Unbalanced"
        open_list = ["[","{","("] 
        close_list = ["]","}",")"]
        myStack = Stack() 
        for i in user_input: 
            if i in open_list: 
                myStack.push(i) 
            elif i in close_list: 
                pos = close_list.index(i) 
                if (myStack.size() > 0) and (open_list[pos] == myStack.peek()): 
                    myStack.pop() 
                else: 
                    return "Unbalanced"
        if myStack.size() == 0: 
            return "Balanced"
        else:
            return "Unbalanced"

b = BalanceParentheses()
user_input = input('Enter your expression : ')
output = b.is_balanced(user_input)
print(output)