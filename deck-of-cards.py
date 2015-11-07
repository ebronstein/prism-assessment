from random import shuffle

SUITS = ["clubs", "hearts", "spades", "diamonds"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]

class Card:

	def __init__(self, suit, rank):
		assert suit.lower() in SUITS, "Not a valid suit"
		assert rank.lower() in RANKS, "Not a valid rank"
		self.suit = suit
		self.rank = rank

	def __repr__(self):
		return ("{0} of {1}".format(self.rank, self.suit))

	def __str__(self):
		return ("{0} of {1}".format(self.rank, self.suit))

ALL_CARDS = [Card(suit, rank) for suit in SUITS for rank in RANKS]

class Deck:

	def __init__(self, cards=ALL_CARDS):
		self.cards = cards

	def Shuffle(self):
		self.cards = ALL_CARDS
		shuffle(self.cards)
		return self.cards

	def GetNextCard(self):
		if not len(self.cards):
			return "Error! Deck is empty."
		return self.cards.pop()

	def __len__(self):
		return len(self.cards)

	def __repr__(self):
		if not len(self.cards):
			return "Empty deck"
		return ", ".join([str(card) for card in self.cards])

	def __str__(self):
		if not len(self.cards):
			return "Empty deck"
		return ", ".join([str(card) for card in self.cards])