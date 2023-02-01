# Homework 4

## Problem 1

In JavaScript, the Array datatype is similar to Python's `list`, but provides different methods, some of which Python doesn't have.

For this problem, you will write a subclass of `list` that provides some of these additional methods.

The class should be named `ESArray` and inherit from the built-in `list` class.

As an extension of `list`, you have access to the built-in methods, including its `__init__`.  Your ESArray therefore is a `list`.  It is important to understand this while implementing the below.

Place your solution in `esarray/esarray.py`.

You can test your solution by running `pytest esarray`.

### Specifications:

- `join` should accept a string, with a single argument `s` and return a string that results from joining each item in the list by the string `s`.
- `every` executes a provided function once for each item in the list, and return `True` if the function returns a true value for each element in the list, and `False` otherwise.
- `for_each` executes a provided function once for each item in the list.  It returns `None`.
- `flatten` returns a **new** `ESArray` with all list-like items in the original flattened.

### Examples:

```python
>>> from esarray import ESArray
>>> x = ESArray([1, -3, 10, 5])

>>> x.join("~~")
1~~-3~~10~~5

# -3 is less than 0
>>> x.every(lambda v: v > 0)
False

# each int in the list is nonzero (truthiness)
>>> x.every(lambda v: v)
True

>>> x.for_each(print)
1
-3
10
5

>>> y = ESArray([[3, 4], [5], 6, [7, [8, [9, 10]]]])
>>> y.flatten()
[3, 4, 5, 6, 7, 8, 9, 10]
>>> y   # y is not changed
[[3, 4], [5], 6, [7, [8, [9, 10]]]]
```

## Problem 2

For Problem 2, you will gain more practice building classes in Python and also give you the opportunity to build an actual application on your own.

In this application, you will build a simple version of the card game, Blackjack with a tkinter GUI. The classes in the game will include: a `Card`, a `Deck`, a `Hand` and a `Game`. On your own (without my guidance), you will determine how to put these classes together to build the actual game.

### Simplified Blackjack Rules

The rules for Blackjack can be quite extensive, however, for this assignment you will only implement the rules below:

- There will be two players in the game, the player, and the dealer.
- Cards 2-10 are worth the value on the card.
- Face cards, Jack, Queen, King, are worth 10.
- An Ace is always worth 11 points in our game.

A round will go through the following process:

1. The deck is shuffled.
2. The player and dealer each recieve two cards from the deck.
3. The player's turn comes first:
  - The player is shown the value of their hand (the sum of card values) and can choose to take another card from the deck (hit) or stop at the current value (stand).
  - If the player chooses to hit, they are given a new card and the total is recalculated.
  - If the player's score is above 21, the player loses (bust).
  - The player may repeat this process until they choose to stand, or bust.
4. If the player did not bust, the dealer plays.
  - The dealer plays automatically, choosing to hit while their hand's value is less than 17.  (i.e. The dealer automatically stands on 17 and above.)
5. If the player and dealer both avoided a bust, then the hand with the highest value wins the game.
   If they have the same hand value, the hand is a tie (push).


### Requirements

#### `Card`

Implement a `Card` class to reprsent a single card. The `Card` class must have the following attributes/methods/properties:

First, define the following constant class attributes:

```
  CLUBS = "clubs"
  DIAMONDS = "diamonds"
  HEARTS = "hearts"
  SPADES = "spades"
  SUIT_SYMBOLS = {
      CLUBS: "♣",
      SPADES: "♠",
      HEARTS: "♥",
      DIAMONDS: "♦",
  }
```

A card class will hold the information on a single card, its `suit`, and `value`.

- `__init__(suit, value)` takes in one of the defined class constants for `suit`, and a value which will be a string
 '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q', or 'A'.
- Define a `@property` named `value` that returns the card numeric value as defined in the rules above.
- Define a `@property` named `color` that returns "red" if the suit is HEARTS or DIAMONDS, and "black" otherwise.
- Define a `@property` named `display` that returns a string with the type of card and suit appended together, for example:
  - `"4♥"` for a four of hearts.
  - `"K♦"` for a king of diamonds.


Place this class inside `blackjack/card.py`.

#### `Hand`

Implement a `Hand` class to reprsent a collection of cards. The `Hand` class must have the following attributes/methods/properties:

- The constructor should take no arguments.  It must define an attribute that will represent your collection of cards. You must decide the appropriate data type for this.
- The method `reset()` should clear the cards in the hand.
- The method `add(card)` should take a `Card` and add it to the hand.
- Define a `@property` named `total`.  This property should return the sum of the values for the cards in the hand according to the rules specified above.

Place this class inside `blackjack/hand.py`.

#### `Deck`

Implement a `Deck` class, which should hold a collection of cards and be able to shuffle & deal the cards.

The `Deck` class must have at least the following attributes/methods/properties:

- `__init__()` should take no arguments, but should initialize your deck with all 52 cards. You may choose whichever data structure you feel best.
  - After initialization a deck contains 52 Cards: Each of '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q', 'A' in each of the 4 suits.
  - The cards should be shuffled.
  - You will also need to track the already dealt cards.
- Define a `@property` named `size` that returns the number of cards left in the deck.
- Define a `deal()` method that removes the top card from the deck and returns it.
- Define a `shuffle` method.  This method shuffles the already dealt cards and places them at the bottom of the deck.
  - You may use `random.shuffle` to help implement this method.
  - https://docs.python.org/3/library/random.html#random.shuffle

Place this class inside `blackjack/deck.py`.

### Putting It Together

This time you will also be putting the pieces together yourself.  You will implement our simplified blackjack game, according to the rules above and making use of the classes you wrote.

In `blackjack.py`, you will see an incomplete `main()` function as well as two helper functions `draw_card_table` and `does_player_hit`.


You will implement our simplified blackjack game, according to the rules above and make use
of the classes you wrote.

You can run your application by running `poetry run python blackjack/blackjack.py`

**You should only need to make changes to the `main()` function in blackjack.py.**
