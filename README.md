# prism-assessment

deck-of-cards.py README

Design decisions
- Deck is implemented as a class with an instance attribute 'cards' that contains all of the cards in the Deck.
- This makes it simple to access the cards in the Deck and manipulate them using various methods.
- It also models the cards as a stack (which is exactly what a deck of cards is) and makes it easy to "pop" off the top card.
- Card is also a class with two instance attributes: 'suit' and 'rank'
- 'suit' and 'rank' must both be in SUITS and RANKS, respectively, which are lists of all of the possible suits and ranks for a generic deck of cards
- ALL_CARDS is a list of a full deck of cards: 13 cards in each of the 4 suites. Having this global variable makes it easy to form a Deck and Shuffle it as well.
- The various built-in methods such as __str__, __repr__, __len__, etc. have been modified to make it easy to "see" what a Deck and Card look like in the Python interpreter.

Ambiguity
- It wasn't exactly specified how Deck and Card should be implemented, other than the fact that the framework should make it possible to create a class that models a generic deck.
- I think it's easier to model both a card and a deck as classes because that offers the flexibility of treating a Card and a Deck in the way that most suits the program and one's goals.

Making sure it works
- To make sure the framework works, the easiest way is to run the file in an interactive session of the Python interpreter and test out the classes and methods.
- Creating a Card object should work properly, only when both 'suit' and 'rank' are in SUITS and RANKS, respectively.
- Creating a Deck object should also work properly and set the Deck's 'cards' instance attribute.
- The Shuffle() method should properly shuffle the Deck and the GetNextCard() should give the topmost card, erroring if the Deck is empty.
