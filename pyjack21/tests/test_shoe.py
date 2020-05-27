import unittest
from pyjack21.shoe import Shoe, Card, Suit, Rank

class TestShoe(unittest.TestCase):

    def setUp(self):
        self.decks = [1, 2, 4, 6]
        self.shoe = Shoe(1)

    def test_init(self):
        for deck in self.decks:
            shoe = Shoe(deck)
            self.assertEqual(deck * 52, len(shoe.cards))
            self.assertEqual(deck, shoe.deck_count)

    def test_deal(self):
        card = self.shoe.deal()
        self.assertTrue(isinstance(card, Card))
        self.assertEqual(51, len(self.shoe.cards))
        self.assertEqual(1, len(self.shoe.discard_shown))

    def test_burn(self):
        self.shoe.burn()
        self.assertEqual(1, len(self.shoe.discard_hidden))
        self.assertEqual(51, len(self.shoe.cards))
        for i in range(52):
            self.shoe.burn()
        self.assertEqual(0, len(self.shoe.cards))

    def test_cards_left(self):
        shoe = self.shoe
        for i in range(10):
            shoe.burn()
        self.assertEqual(42, shoe.cards_left())
        for i in range(45):
            shoe.deal()
        self.assertEqual(0, shoe.cards_left())

if __name__ == '__main__':
    unittest.main()
