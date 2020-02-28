import os.path, sys 
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from queueUsingLL import *
from deckOfCard import *

my_queue = QueueUsingLinkedList()
my_deck = Card()

class DeckUsingQueue:
    def checkTen(self,temp_array_card):
        if '10' in temp_array_card:
            return True
        return False
    
    def checkJack(self,temp_array_card):
        if 'J ' in temp_array_card:
            return True
        return False
    
    def checkQueen(self,temp_array_card):
        if 'Q ' in temp_array_card:
            return True
        return False
    
    def checkKing(self,temp_array_card):
        if 'K ' in temp_array_card:
            return True
        return False
    
    def checkAce(self,temp_array_card):
        if 'A ' in temp_array_card:
            return True
        return False

    def addFaceCardToQueue(self,temp_array_card,temp_array_rank):
        while self.checkTen(temp_array_card):
            index = temp_array_card.index('10')
            temp_array_card.pop(index)
            my_card = temp_array_rank.pop(index)
            my_queue.enque(my_card)
        while self.checkJack(temp_array_card):
            index = temp_array_card.index('J ')
            temp_array_card.pop(index)
            my_card = temp_array_rank.pop(index)
            my_queue.enque(my_card)
        while self.checkQueen(temp_array_card):
            index = temp_array_card.index('Q ')
            temp_array_card.pop(index)
            my_card = temp_array_rank.pop(index)
            my_queue.enque(my_card)
        while self.checkKing(temp_array_card):
            index = temp_array_card.index('K ')
            temp_array_card.pop(index)
            my_card = temp_array_rank.pop(index) 
            my_queue.enque(my_card)                
        while self.checkAce(temp_array_card):
            index = temp_array_card.index('A ')
            temp_array_card.pop(index)
            my_card = temp_array_rank.pop(index)  
            my_queue.enque(my_card)                 

    def addToQueue(self,deck,number_of_players):
        higher_card = ["10","J ","Q ","K ","A "]
        for row in deck:
            player = 'player'+' '+str(number_of_players)+':'
            temp_array_card = []
            temp_array_rank = []
            row.sort()
            for j in range(len(row)):
                next_card = str(row[j])
                card = next_card[0:2]
                if j == 0:
                    my_queue.enque(player)
                if card == 'pl':
                    continue
                elif card not in higher_card:
                    my_queue.enque(next_card)
                else:
                    temp_array_card.append(card)
                    temp_array_rank.append(next_card)
            self.addFaceCardToQueue(temp_array_card,temp_array_rank)
            number_of_players -= 1
        my_queue.enque(0)

if __name__ == "__main__":
    new_obj = DeckUsingQueue()
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
        card_per_player = number_of_cards//number_of_players
        deck = my_deck.distribute(number_of_cards,number_of_players)
        new_obj.addToQueue(deck,number_of_players)
        while my_queue.size() != 0:
            card = my_queue.dequeue()
            print(card,end=",")
            if my_queue.size() % (card_per_player+1) == 0:
                print()
        break

