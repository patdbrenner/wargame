'''Card Game: WAR'''
import random

suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
          'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card():
    '''Playing card'''
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        '''Allow printing of card class'''
        return self.rank + ' of ' + self.suit

class Deck():
    '''Deck of playing cards'''
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(rank, suit)

                self.all_cards.append(created_card)

    def shuffle(self):
        '''Shuffle deck'''
        random.shuffle(self.all_cards)

    def deal_one(self):
        '''Deal one card to player's hand'''
        return self.all_cards.pop()

class Player():
    '''Player class'''
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        '''Removes top card for player'''
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        '''Adds played cards to player's hand'''
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        '''Prints the number of cards player has'''
        if len(self.all_cards) != 1:
            return f'{self.name} has {len(self.all_cards)} cards.'
        else:
            return f'{self.name} has 1 card.'

player_one = Player('Luna')
player_two = Player('Hunter')

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

GAME_ON = True

ROUND_NUM = 0

while GAME_ON:

    ROUND_NUM += 1
    print(f'Round {ROUND_NUM}')

    if len(player_one.all_cards) == 0:
        print('Luna is out of cards! Hunter wins!')
        GAME_ON = False
        break
    if len(player_two.all_cards) == 0:
        print('Hunter is out of cards! Luna wins!')
        GAME_ON = False
        break

    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    COMPARING = True

    while COMPARING:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            print(f"Luna's {player_one_cards[-1]} beats Hunter's {player_two_cards[-1]}")
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            COMPARING = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            print(f"Hunter's {player_two_cards[-1]} beats Luna's {player_one_cards[-1]}")
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)
            COMPARING = False
        else:
            print('WAR')
            if 0 < len(player_one.all_cards) < 5:
                for num in range(len(player_one.all_cards)):
                    player_one_cards.append(player_one.remove_one())
            if 0 < len(player_two.all_cards) < 5:
                for num in range(len(player_two.all_cards)):
                    player_two_cards.append(player_two.remove_one())
            elif len(player_one.all_cards) == 0:
                print('Luna is out of cards! Hunter wins!')
                GAME_ON = False
                break
            elif len(player_two.all_cards) == 0:
                print('Hunter is out of cards! Luna wins!')
                GAME_ON = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
