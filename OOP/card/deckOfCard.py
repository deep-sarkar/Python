import random

class Card:
    def __init__(self):
        self.cards = ['2 ','3 ','4 ','5 ','6 ','7 ','8 ','9 ','10','J ','Q ','K ','A ']
        self.suites = ['♥','♠','♣','♦']
    
    '''
        -makeDeck(self) method will make a deck by takin cards and suits and return complete deck
    '''
    def makeDeck(self):
        deck = []
        for suit in self.suites:
            for card in self.cards:
                next_card = card +' '+ suit
                deck.append(next_card)
        return deck

    '''
        -distribute(self, number_of_cards, number_of_players) method will distribute shuffled card
            according to number of players
    '''    
    def distribute(self, number_of_cards, number_of_players):
        row = number_of_players
        column = number_of_cards//row
        deck = self.makeDeck()
        random.shuffle(deck)
        distribute_card = []
        player_hand = []
        player = 'player'+' '+str(number_of_players)+':'
        player_hand.append(player)
        j = 0
        for card in deck:
            player_hand.append(card)
            j += 1
            number_of_cards -= 1
            if j == column :
                number_of_players -= 1
                player = 'player'+' '+str(number_of_players)+':'
                distribute_card.append(player_hand)
                player_hand = []
                player_hand.append(player)
                j = 0
            if number_of_cards == 0:
                break
        return distribute_card

# main method
if __name__ == "__main__":
    my_deck = Card()
    while True:
        try:
            number_of_cards = int(input('Total card : '))
            number_of_players = int(input('Total players : '))
            if number_of_cards < 1 > number_of_players or number_of_cards > 52:
                print('Please enter proper value ')
                continue
        except ValueError:
            print('Please enter proper number format')
            continue
        deck = my_deck.distribute(number_of_cards,number_of_players)
        for row in deck:
            print(row)
        break


                        
