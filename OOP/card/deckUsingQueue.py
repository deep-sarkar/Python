import os.path, sys 
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from queueUsingLL import *
from deckOfCard import *

my_queue = QueueUsingLinkedList()
my_deck = Card()
class DeckUsingQueue:
    def addToQueue(self,deck,number_of_players):
        higher_card = ["10","j","Q","K","A"]
        player = 'player'+' '+str(number_of_players)+':'
        for row in deck:
            temp_array1 = []
            temp_array2 = []
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
                    temp_array1.append(card)
                    temp_array2.append(next_card)
            if '10' in temp_array1:
                index = temp_array1.index('10')
                my_queue.enque(temp_array2[index])
            if 'J ' in temp_array1:
                index = temp_array1.index('J ')
                my_queue.enque(temp_array2[index])
            if 'Q ' in temp_array1:
                index = temp_array1.index('Q ')
                my_queue.enque(temp_array2[index])
            if 'K ' in temp_array1:
                index = temp_array1.index('K ')
                my_queue.enque(temp_array2[index])
            if 'A ' in temp_array1:
                index = temp_array1.index('A ')
                my_queue.enque(temp_array2[index])
            number_of_players -= 1

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

        for i in range(number_of_cards):
            card = my_queue.dequeue()
            print(card,end=",")
            if number_of_cards % card_per_player == 0:
                print()
        break

