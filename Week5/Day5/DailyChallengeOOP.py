# Part 1 : Quizz : Answer the following questions

# What is a class?
# What is an instance?
# What is encapsulation?
# What is abstraction?
# What is inheritance?
# What is multiple inheritance?
# What is polymorphism?
# What is method resolution order or MRO?

import random
# Instructions
# Part 2: Create a deck of cards class.
class Cards():
    def __init__(self,suit,value):
        self.suit=suit
        self.value=value  
    
    def show(self):
        print(f"The {self.value} of {self.suit}")
# The deck of cards class should inherit from a card class.
# The requirements are as follows:
class Deck(Cards):
    def __init__(self, suit,value):
        super().__init__(suit,value)
        self.cards[]
        
    def create_deck(self):
        for suit in ["Hearts","Diamonds","Spades","Clubs"]:
            for value in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]:
                self.cards.append(Card(suit,value))
                
    def deal(self):
        pass
    
    def shuffle(self):
        return random.shuffle(self.cards)
# The Deck class should have a method called deal which deals a single card from the deck.
# After a card is dealt, it should be removed from the deck.
# There should be a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)