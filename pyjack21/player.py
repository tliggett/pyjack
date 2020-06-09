import json

from pyjack21.shoe import Shoe, Card, Rank, Suit
from pyjack21.human import get_human



class Hand:
    def __init__(self, cards=[]):
        """
        class hand stores a hand of cards
        """
        self.hand = []
        for card in cards:
            self.deal(card)


    def deal(self, card: Card):
        self.hand.append(card)

    def hand_value(self, hand=None):
        """
        returns the value of the player's hand
        :param hand: a hand of cards
        """
        if hand is None:
            hand = self.hand
        hand = sorted(hand)
        value = 0
        # First calculate the soft value of a hand
        first_ace = True
        for card in hand:
            if first_ace:
                value += card.value()
                if card.value() == 11:
                    first_ace = False
            else:
               value += card.value(aces_high=False)
        # if the soft value busts, convert to hard value
        if value > 21:
            value = 0
            for card in hand:
                value += card.value(aces_high=False)

        return value

    def hand_str(self):
        """
        returns a string representation of the hand:
        (examples -> two cards: A2, 5K | 3+ cards: H16, S17)
        return: string representation of the hand
        """
        hand_s = sorted(self.hand)
        handstr = ""
        # handle two card hands
        for card in hand_s:
            handstr += card.char_rep()
        # handle 3+ card hands
        if len(self.hand) > 2:
            if "A" not in handstr:
                handstr = f'H{self.hand_value()}'
            elif self.__hand_is_soft():
                handstr = f'S{self.hand_value()}'
            else:
                handstr = f'H{self.hand_value()}'
        return handstr

    def hand_key(self):
        hand_s = sorted(self.hand)
        hand_key = ""
        for card in hand_s:
            hand_key += card.char_rep()
        if self.__hand_is_pair():
            hand_key = f'{hand_key}'
        elif 'A' in hand_key and self.__hand_is_soft():
            hand_key = f'S{self.hand_value()}'
        else:
            hand_key=f'H{self.hand_value()}'
        return hand_key

    def __hand_is_soft(self):
        """
        determines whether a hand is soft
        :returns: true or false depending on soft
        """
        hard_value = self.__get_aces() + self.hand_value(self.__pull_aces())
        # print(self.hand)
        if hard_value <= 11:
            return True
        return False

    def __hand_is_pair(self):
        if len(self.hand) > 2:
            return False
        if self.hand[0] == self.hand[1]:
            return True

    def __pull_aces(self, hand=None):
        """
        Takes the aces out of a hand and returns the aceless hand
        :param hand: hand of cards
        :return: a hand of cards without aces
        """
        if hand is None:
            hand = self.hand
        no_aces = []
        for card in hand:
            if card.get_rank() is not Rank.ace:
                no_aces.append(card)
        return no_aces


    def __get_aces(self):
        """
        counts the aces in a hand
        :return: number of aces in hand
        """
        hand_s = sorted(self.hand)
        ace_count = 0
        for card in hand_s:
            if card.get_rank() == Rank.ace:
                ace_count = ace_count + 1
        return ace_count


class Player:
    def __init__(self, payroll=500):
        """
        initializes a player for blackjack
        :param payroll: blackjack player payroll
        """

        self.hands = [] # The player's hand of cards.
        self.type = 'human' # player type. will allow for ai types later
        self.payroll = payroll # player's remaining money 
        self.wager = 0  # player's wager for current hand
        self.moves = get_human()
        '''
        with open('pyjack21/data/human.json') as f:
            self.moves = json.load(f)
        '''

    def dealer_card(self):
        return self.hands[0].hand[0]

    def bet(self, minimum=10):
        """
        returns the bet of the player
        :param minimum: the minimum bet for the hand
        :return: the bet of the player
        """
        if minimum > self.payroll:
            self.wager = 0
        else:
            self.payroll = self.payroll - minimum
            self.wager = minimum
        return minimum

    def deal_hand(self, hand: Hand):
        self.hands.append(hand)
    
    def deal_hand_cards(self, cards=[]):
        hand = Hand()
        for card in cards:
            hand.append(card)
        self.hands.append(hand)

    def move(self, shoe: Shoe, hand: Hand, dealer_card: Card):
        """
        player plays current hand and decides move
        :param shoe: the shoe of cards in player
        :param dealer_card: the card of the dealer
        """
        move = ""
        if hand.hand_value() > 21:
            move = "BUST"
        elif hand.hand_value() == 21:
            if len(hand.hand) == 2:
                move = "BLACKJACK"
            else:
                move = "S"
        else:
             move = self.moves["hand"][hand.hand_key()][dealer_card.char_rep()]
        # print(f'{self.hand_value()} : {move}')
        return move

    def pay(self, payout):
        """
        pays the player and resets their wager
        :param payout: amount to pay the player
        """
        self.payroll = self.payroll + payout
        self.wager = 0




if __name__ == "__main__":
    izzy = Player()
    shoe = Shoe(6)
    shoe.shuffle()
    shoe.burn()
    dealer_card = shoe.deal()
    print(f'Dealer card: {dealer_card.char_rep()}')
    izzy.hand.append(shoe.deal())
    izzy.hand.append(shoe.deal())
    print(f'{izzy.hand_str()}')
    print(f'{izzy.hand_key()}')
    print(f'{izzy.play(shoe, dealer_card)}')
    while izzy.play(shoe, dealer_card) == "H":
       izzy.hand.append(shoe.deal())
       print(f'{izzy.hand_str()}')

    print(f'Final Hand Value: {izzy.hand_value()}')

