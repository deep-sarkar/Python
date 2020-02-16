class MagicNumber:
    def find_number(self,low,high):
        if low < high :
            mid = (low + high) // 2
            print('if your number is between ',(mid + 1),' and ',high,' press \'Y\'')
            user_input = input(' : ')
            if user_input == 'Y' or user_input == 'y':
                low = mid
                return self.find_number(mid + 1,high)
            else :
                return self.find_number(low,mid)
        return high

fn = MagicNumber()
number = int(input('Enter a number n : '))
print('Guess a number between 1 to ',number)
guessed_number = fn.find_number(1, number)
print('your number is : ',guessed_number)
