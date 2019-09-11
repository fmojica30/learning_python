# File: Blackjack.py

# Description:

# Student's Name: Fernando Martinez Mojica

# Student's UT EID: fmm566

# Course Name: CS 313E

# Unique Number: 50725

# Date Created: 2/21/19

# Date Last Modified: 2/24/19

import random

class Card(object):

    RANKS = (1,2,3,4,5,6,7,8,9,10,11,12,13)

    SUITS = ('C','D','H','S')

    def __init__(self,rank = 12, suit = 'S'):

        if (rank in Card.RANKS):

            self.rank = rank

        else:

            self.rank = 12

        if (suit in Card.SUITS):

            self.suit = suit

        else:

            self.suit = 'S'

    def __str__(self):

        if self.rank == 14:

            rank = 'A'

        elif self.rank == 13:

            rank = 'K'

        elif self.rank == 12:

            rank = 'Q'

        elif self.rank == 11:

            rank = 'J'

        else:

            rank = str(self.rank)

        return rank + self.suit

    def __eq__(self,other):

        return self.rank == other.rank

    def __ne__(self,other):

        return self.rank != other.rank

    def __lt__(self,other):

        return self.rank < other.rank

    def __le__(self,other):

        return self.rank <= other.rank

    def __gt__(self,other):

        return self.rank > other.rank

    def __ge__(self,other):

        return self.rank >= other.rank

class Deck(object):

    def __init__(self,num_decks = 1):

        self.deck = []

        for i in range(num_decks):

            for suit in Card.SUITS:

                for rank in Card.RANKS:

                    card = Card(rank,suit)

                    self.deck.append(card)

    #shuffle the deck

    def shuffle(self):

        random.shuffle(self.deck)

    def deal(self):

        if len(self.deck) == 0:

            return none

        else:

            return self.deck.pop(0)

class Player(object):

    #cards is a list of Card objects
    def __init__(self,cards):

        self.cards = cards

    #when a player hits append a card
    def hit(self,card):

        self.cards.append(card)

    def get_points(self):

        count = 0

        for card in self.cards:

            if (card.rank > 9):

                count += 10

            elif (card.rank == 1):

                count += 11

            else:

                count += card.rank

    #deduct 10 if ace is there and needed as 1
        for card in self.cards:

            if count <= 21:

                break

            elif(card.rank == 1):

                count -= 10

        return count

    #define if the player has a blackjack
    def has_blackjack(self):

        return (len(self.cards) == 2 and (self.get_points() == 21))

    #complete str funtion that returns cards and the points

    def __str__(self):

        hand_str = ''

        for card in self.cards:

            hand_str = hand_str + str(card) + ' '

        return hand_str + ' ' + 'Points' + ' - ' + str(self.get_points())




class Dealer(Player):

    def __init__(self,cards):

        Player.__init__(self,cards)

        self.show_one_card = True

    def hit(self,deck):

        self.show_one_card = False

        while (self.get_points() < 17):

            self.cards.append(deck.deal())

    def __str__(self):

        if self.show_one_card == True:

            return str(self.cards[0])

        else:

            return Player.__str__(self)

class Blackjack(object):

    def __init__(self,num_players = 1):

        self.deck = Deck()

        self.deck.shuffle()

        #create player objects

        self.num_players = num_players

        self.player_list = []

        for i in range(self.num_players):

            player = Player([self.deck.deal(),self.deck.deal()])

            self.player_list.append(player)

        #create dealer object dealer also gets two cards

        self.dealer = Dealer([self.deck.deal(),self.deck.deal()])

    def play(self):

        #find out what points they have

        for i in range(self.num_players):

            print('Player ' + str(i+1) + ':' + str(self.player_list[i]))

        #print the card the dealer has

        print('Dealer ' + str(self.dealer))

        print('')

        #main part

        player_points = []

        for i in range(self.num_players):

            choice = input('Player ' + str(i+1) + ': ' + 'Do you want to hit? [y / n]:')

            while True:

                if choice in ['y','Y']:

                    (self.player_list[i]).hit(self.deck.deal())

                    points = (self.player_list[i]).get_points()

                    print('Player ' + str(i + 1) + ':' + str(self.player_list[i]))

                    if (points >= 21):

                        print('') #putting space between each turn

                        player_points.append(points)

                        break

                    choice = input('Player ' + str(i+1) + ': ' + 'Do you want to hit? [y / n]:')

                else:

                    points = (self.player_list[i]).get_points()

                    player_points.append(points)

                    print('')

                    break

        self.dealer.hit(self.deck)

        #dealers turn to hit

        dealer_points = self.dealer.get_points()

        print('Dealer:' + str(self.dealer))

        #determining if the player beat the dealer or vice versa and printing

        for player in player_points:

            if dealer_points > 21:

                if player <= 21:

                    print('Player ' + str(player_points.index(player) + 1) + ' wins')

                else:

                    print('Player ' + str(player_points.index(player) + 1) + ' looses')

            if dealer_points <= 21:

                if player == dealer_points:

                    print('Player ' + str(player_points.index(player) + 1) + ' ties')

                elif (player > dealer_points) and (player <= 21):

                    print('Player ' + str(player_points.index(player) + 1) + ' wins')

                elif (player > dealer_points) and (player > 21):

                    print('Player ' + str(player_points.index(player) + 1) + ' loses')

                elif player < dealer_points:

                    print('Player ' + str(player_points.index(player) + 1) + ' loses')




def main():

    num_players = int(input('Enter number of players: '))

    if num_players >= 2 and num_players <= 6:

        game = Blackjack(num_players)

        game.play()

    else:

        num_players = int(input('Enter a valid number of players: '))


        #validation = str(input('Do you want to play blackjack? [y/n]'))



main()
