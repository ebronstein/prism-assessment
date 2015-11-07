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


vacationing-salesman README

How to run the script
python3 vacationing_salesman.py [-h] [-m] [-k] < my_cities_file.txt

optional arguments:
  -h, --help        show this help message and exit
  -m, --miles       see the output in miles
  -k, --kilometers  see the output in kilometers

cities_file.txt should be a .txt file containing one city per line in the format "City, Country"

Why I chose Python
- The main reason is that I know Python the best, so it was the easiest to make this script in.
- Also, it was simple to implement the geopy library to calculate distances, so that was another incentive to use Python.

Design decisions
- I used the geopy library to geocode the locations and calculate the distances between them. It has very good documentation and is simple to implement, so I decided that it would be a good fit for this script.
- When the script is run, it first checks for the optional format arguments, which dictate whether the itinerary will be printed in miles or kilometers.
- From there, it calls make_itinerary(format) in order to parse the text file and extract the names of the cities.
- Next, it calls get_distances(cities, format), which uses the geopy library to convert the cities to geolocations and then calculate the distances between each of them in the specified format (miles or kilometers). It returns the distances in a list.
- Finally, the script calls print_itinerary(cities, distances, format) to print the itinerary in the proper format.
- I decided it was easiest to break up the program into these separate functions in order to make it modular and easier to debug.
- I used lists to store cities, geolocations, and distances because that was the simplest data structure to store itinerary items in for later iteration.

If I had more time
- Unfortnately, I didn't have time to implement all of the bonus parts that I wanted, but here is what I would do if I had had more time.
- First, I would most likely switch to a different library or API for geolocation because I don't believe geopy allows the option of setting the mode of transportation, such as walking, driving, kayaking, etc.
- Second, I would implement the option to set the mode of transportation. I would do this through optional command-line arguments such as --kayak, --walk, --drive, etc. and use the geolocation library or API to calculate the time properly.
- Third, I would work on optimizing the itinerary. I believe there are APIs out there (perhaps Google Maps?) that have optimization functions that minimize the amount of time traveled by changing the order of the location visisted, but I would have to look into that. If such a function doesn't exist, I would try implementing my own method of doing it. The first (probably crude) way that comes to mind is the following: start at the first location and sort the distances by smallest to largest. Go to the closest location and remove the 2 location that you've visited, as well as the distance you traveled. Next, sort the rest of the distances list from smallest to largest and go to the closest destination. Repeat this process until you've visited all of the destinations. I'm sure there is a better way of doing this, but I would need a bit more time to think about the most efficient way of planning one's itinerary.
