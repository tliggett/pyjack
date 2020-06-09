import unittest

from pyjack21.shoe import Card, Rank, Suit
from pyjack21.player import Hand


class TestHand(unittest.TestCase):

    def setUp(self):
        self.hand = Hand()
    
        cards = {}
        cards['ace'] = Card(Suit.heart, Rank.ace)
        cards['four'] = Card(Suit.club, Rank.four)
        cards['three'] = Card(Suit.club, Rank.three)
        cards['nine'] = Card(Suit.diamond, Rank.nine)
        cards['ten'] = Card(Suit.spade, Rank.ten)
        cards['queen'] = Card(Suit.spade, Rank.queen)
        cards['king'] = Card(Suit.diamond, Rank.king)
        self.cards = cards

    def test_hand_value(self):
        hand = self.hand
        cards = self.cards
        # test ace hands
        hand.deal(cards['ace'])
        hand.deal(cards['four'])
        self.assertEqual(15, hand.hand_value())
        hand.deal(cards['four'])
        self.assertEqual(19, hand.hand_value())
        hand.deal(cards['three'])
        self.assertEqual(12, hand.hand_value())
        # test hard hands
        hand.hand = []
        hand.deal(cards['nine'])
        hand.deal(cards['king'])
        self.assertEqual(19, hand.hand_value())
        hand.deal(cards['three'])
        self.assertEqual(22, hand.hand_value())

    def test_deal(self):
        hand = self.hand
        cards = self.cards
        hand.deal(cards['ace'])
        self.assertEqual(hand.hand[0], cards['ace'])

    def test_hand_str(self):
        keys = ['A3', 'S18', 'H18', 'H22', '3K', 'H17']
        hand = self.hand
        cards = self.cards
        # test ace hands
        hand.deal(cards['three'])
        hand.deal(cards['ace'])
        self.assertEqual(hand.hand_str(), keys[0])
        hand.deal(cards['four'])
        self.assertEqual(hand.hand_str(), keys[1])
        hand.deal(cards['queen'])
        self.assertEqual(hand.hand_str(), keys[2])
        hand.deal(cards['four'])
        self.assertEqual(hand.hand_str(), keys[3])
        # test hard hands
        hand.hand = []
        hand.deal(cards['king'])
        hand.deal(cards['three'])
        self.assertEqual(hand.hand_str(), keys[4])
        hand.deal(cards['four'])
        self.assertEqual(hand.hand_str(), keys[5])

    def test_hand_key(self):
        keys = ['S14', 'S18', 'H18', 'H22', 'H13', 'H17', '44', 'QQ']
        hand = self.hand
        cards = self.cards
        # test ace hands
        hand.deal(cards['three'])
        hand.deal(cards['ace'])
        self.assertEqual(hand.hand_key(), keys[0])
        hand.deal(cards['four'])
        self.assertEqual(hand.hand_key(), keys[1])
        hand.deal(cards['queen'])
        self.assertEqual(hand.hand_key(), keys[2])
        hand.deal(cards['four'])
        self.assertEqual(hand.hand_key(), keys[3])
        # test hard hands
        hand.hand = []
        hand.deal(cards['king'])
        hand.deal(cards['three'])
        self.assertEqual(hand.hand_key(), keys[4])
        hand.deal(cards['four'])
        self.assertEqual(hand.hand_key(), keys[5])
        hand.hand = []
        hand.deal(cards['four'])
        hand.deal(cards['four'])
        self.assertEqual(hand.hand_key(), keys[6])
        hand.hand = []
        hand.deal(cards['queen'])
        hand.deal(cards['queen'])
        self.assertEqual(hand.hand_key(), keys[7])