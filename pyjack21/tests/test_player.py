import unittest

from pyjack21.player import Player, Hand
from pyjack21.shoe import Card, Rank, Suit


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player(payroll=500)
        cards = {}
        cards['ace'] = Card(Suit.heart, Rank.ace)
        cards['four'] = Card(Suit.club, Rank.four)
        cards['three'] = Card(Suit.club, Rank.three)
        cards['nine'] = Card(Suit.diamond, Rank.nine)
        cards['ten'] = Card(Suit.spade, Rank.ten)
        cards['queen'] = Card(Suit.spade, Rank.queen)
        cards['king'] = Card(Suit.diamond, Rank.king)
        self.cards = cards

    def test_bet(self):
        player = self.player
        player.bet(minimum=10)
        self.assertEqual(10, player.wager)
        self.assertEqual(490, player.payroll)

    def test_deal_hand(self):
        player = self.player
        cards = self.cards
        hand = Hand()
        hand.deal(cards['four'])
        hand.deal(cards['three'])
        player.deal_hand(hand)
        self.assertEqual(player.hands[0], hand)

    def test_deal_hand_cards(self):
        player = self.player
        cards = self.cards
        hand_cards = []
        hand_cards.append(cards['four'])
        hand_cards.append(cards['three'])
        player.deal_hand_cards(hand_cards)
        for hand_card, card in player.hands[0], hand_cards:
            self.assertEqual(player.hands[0], hand_cards)

    def test_pay(self):
        player = self.player
        player.wager = 10
        player.pay(player.wager)
        self.assertEqual(510, player.payroll)
        self.assertEqual(0, player.wager)
