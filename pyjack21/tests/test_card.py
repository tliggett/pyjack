import unittest
from pyjack21.shoe import Card, Suit, Rank

class TestCard(unittest.TestCase):

    def test_suit(self):
        for suit in Suit:
            card = Card(suit, Rank.four)
            self.assertEqual(suit, card.get_suit())

    def test_rank(self):
        for rank in Rank:
            card = Card(Suit.club, rank)
            self.assertEqual(rank, card.get_rank())

    def test_char_rep(self):
        chars = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
        for rank, char in zip(Rank, chars):
            card = Card(Suit.club, rank)
            self.assertEqual(char, card.char_rep())

    def test_value(self):
        values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        # test card values
        for rank, value in zip(Rank, values):
            card = Card(Suit.club, rank)
            self.assertEqual(value, card.value())
        # test low ace
        card = Card(Suit.heart, Rank.ace)
        self.assertEqual(1, card.value(aces_high=False))

    def test_card_comparisons(self):
        cards = [ Card(Suit.club, Rank.four),       # 0
                  Card(Suit.club, Rank.three),      # 1
                  Card(Suit.heart, Rank.ace),       # 2
                  Card(Suit.spade, Rank.ace),       # 3
                  Card(Suit.diamond, Rank.ace),     # 4
                  Card(Suit.heart, Rank.five),      # 5
                  Card(Suit.spade, Rank.ten),       # 6
                  Card(Suit.spade, Rank.jack),      # 7
                  Card(Suit.diamond, Rank.queen),   # 8
                  Card(Suit.diamond, Rank.king),    # 9
                ]

        self.assertTrue(cards[1] == cards[1])
        self.assertFalse(cards[0] == cards[1])

        self.assertTrue(cards[0] > cards[1])
        self.assertFalse(cards[6] > cards[7])

        self.assertTrue(cards[1] < cards[0])
        self.assertFalse(cards[0] < cards[1])

        self.assertTrue(cards[2] <= cards[3])
        self.assertFalse(cards[0] <= cards[1])

        self.assertTrue(cards[9] >= cards[8])
        self.assertFalse(cards[8] >= cards[9])

        self.assertTrue(cards[0] != cards[1])
        self.assertFalse(cards[2] != cards[3])

if __name__ == '__main__':
    unittest.main()
