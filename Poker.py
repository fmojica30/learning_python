import random

class Card(object):

    RANKS = (2,3,4,5,6,7,8,9,10,11,12,13,14)

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

class Poker(object):

    def __init__(self,num_players = 2, num_cards = 5):

        self.deck = Deck()

        self.deck.shuffle()

        self.num_players = num_players

        self.all_hands = []

        self.numCards_in_hand = num_cards

    #deal a hand to the players

        for i in range(self.num_players):

            hand = []

            self.all_hands.append(hand)

        for j in range(self.numCards_in_hand):

            for k in range(self.num_players):

                self.all_hands[k].append(self.deck.deal())

    def play(self):

        for i in range(len(self.all_hands)):

            sorted_hand = sorted(self.all_hands[i], reverse = True)

            self.all_hands[i] = sorted_hand

            hand_str = ''

            for card in sorted_hand:

                hand_str = hand_str + str(card) + ' '

            print('Player' + str(i + 1) + ': ' + hand_str)

            hand_type = []

            hand_points = []

    #def is a royal flush
    #takes as argument a hand and returns point for that hand

    def is_royal(self,hand):

        same_suit = True

        for i in range(len(hand)):

            same_suit = same_suit and (hand[i].suit == hand[i+1])

        if (not same_suit):

            return 0 , ''

        rank_order = True

        for i in range(len(hand)):

            rank_order == rank_order and (hand[i].rank == 14 - i)

        if (not rank_order):

            return 0, ''

        points = 10 * (15 ** 5) + (hand[0].rank)*(15**4)  + (hand[1].rank)*(15**3) + (hand[2].rank)*(15**2) + (hand[3].rank)*(15**1) + (hand[4].rank)*(15**0)

        return points, 'Royal Flush'

    #define if hand is one pair

    def is_one_pair(self,hand):

        one_pair = False

        for i in range(len(hand) - 1):

            if (hand[i].rank == hand[i+1].rank):

                one_pair = True

                placeH = hand[0]

                placeH_1 = hand[1]

                hand[0] = hand[i]

                hand[1] = hand[i+1]

                hand[i] = placeH

                hand[i+1] = placeH_1

                break

            if (not one_pair):

                return 0, ''

        points = 2 * (15 ** 5) + (hand[0].rank)*(15**4)  + (hand[1].rank)*(15**3) + (hand[2].rank)*(15**2) + (hand[3].rank)*(15**1) + (hand[4].rank)*(15**0)

        return points, 'One Pair'






def main():

    p1 = Poker()

    p1.play()

main()
