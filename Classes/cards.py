### Playing cards
# There are fifty-two cards in a deck, each of which belongs to one of four suits and 
# one of thirteen ranks. The suits are Spades, Hearts, Diamonds, and Clubs (in descending 
# order in bridge). The ranks are Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, and King. 
# Depending on the game that we are playing, the rank of Ace may be higher than King or 
# lower than 2. The rank is sometimes called the face-value of the card.

class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])
    
    def from_str(self, text):
        l = text.split(" ")
        if len(l) != 3: return None
        rank = 0
        for (i, r) in enumerate(self.ranks):
            if r == l[0]:
                rank = i
        suit = -1
        for (j, s) in enumerate(self.suits):
            if s == l[2]:
                suit = j
        if rank == 0 or suit == -1: return None

        return Card(suit, rank)
    
    def cmp(self, other):
        # Check the suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        # Suits are the same... check ranks

        # Ranks are the same... it's a tie
        if self.rank == other.rank: return 0
        # Aces are ranked higher than Kings
        if self.rank == self.ranks[1] or self.rank == 1: return 1
        if other.rank == self.ranks[1] or other.rank == 1: return -1
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        return 0
    
    def __eq__(self, other):
        return self.cmp(other) == 0

    def __le__(self, other):
        return self.cmp(other) <= 0

    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __ne__(self, other):
        return self.cmp(other) != 0  

### a deck is made up of cards, so each Deck object will contain a list of cards 
# as an attribute. Many card games will need at least two different decks — a red deck and a blue deck.
class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def print_deck(self):
        for card in self.cards:
            print(card)

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + "\n"
        return s
    
    def shuffle(self):
        import random      
        rng = random.Random()        # Create a random generator
        rng.shuffle(self.cards)      # uUse its shuffle method

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True 
        else:
            return False 
        
    def pop(self):
        """ Removes the last card in the list, so we are in effect dealing from the bottom of the deck """
        return self.cards.pop()
    
    def is_empty(self):
        return self.cards == []
    
    def deal(self, hands, num_cards=999):
        num_hands = len(hands)
        for i in range(num_cards):
            if self.is_empty():
                break                    # Break if out of cards
            card = self.pop()            # Take the top card
            hand = hands[i % num_hands]  # Whose turn is next?
            hand.add(card)               # Add the card to the hand

### A hand is similar to a deck, of course. Both are made up of a set of cards, and both require operations 
# like adding and removing cards. Also, we might like the ability to shuffle both decks and hands.
# A hand is also different from a deck. Depending on the game being played, we might want to perform some 
# operations on hands that don’t make sense for a deck. For example, in poker we might classify a hand 
# (straight, flush, etc.) or compare it with another hand. In bridge, we might want to compute a score for 
# a hand in order to make a bid.
class Hand(Deck):
    
    def __init__(self, name=""):
       self.cards = []
       self.name = name

    def add(self, card):
        self.cards.append(card)

    def __str__(self):
        s = "Hand " + self.name
        if self.is_empty():
            s += " is empty\n"
        else:
            s += " contains\n"
        return s + Deck.__str__(self)
    
### The CardGame class takes care of some basic chores common to all games, such as creating the deck and shuffling it
class CardGame:

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

### The object of Old Maid is to get rid of cards in your hand. You do this by matching cards by rank and color. 
# For example, the 4 of Clubs matches the 4 of Spades since both suits are black. The Jack of Hearts matches the 
# Jack of Diamonds since both are red.
# To begin the game, the Queen of Clubs is removed from the deck so that the Queen of Spades has no match. The 
# fifty-one remaining cards are dealt to the players in a round robin. After the deal, all players match and discard 
# as many cards as possible.
# When no more matches can be made, play begins. In turn, each player picks a card (without looking) from the closest 
# neighbor to the left who still has cards. If the chosen card matches a card in the player’s hand, the pair is removed. 
# Otherwise, the card is added to the player’s hand. Eventually all possible matches are made, leaving only the Queen 
# of Spades in the loser’s hand.

class OldMaidHand(Hand):

    def remove_matches(self, print_removals=False):
        count = 0
        original_cards = self.cards[:]
        for card in original_cards:
            # The match card has the same rank and the other suit of the same color
            match = Card(3 - card.suit, card.rank)
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)
                if print_removals:
                    print("Hand {0}: {1} matches {2}".format(self.name, card, match))
                count += 1
        return count
    
class OldMaidGame(CardGame):
    def play(self, names):
        # Remove Queen of Clubs
        self.deck.remove(Card(0,12))

        # Make a hand for each player
        self.hands = []
        for name in names:
            self.hands.append(OldMaidHand(name))

        # Deal the cards
        self.deck.deal(self.hands)
        print("---------- Cards have been dealt")
        self.print_hands()

        # Remove initial matches
        matches = self.remove_all_matches()
        print("---------- Matches discarded, play begins")
        self.print_hands()

        # Play until all 50 cards are matched
        turn = 0
        num_hands = len(self.hands)
        while matches < 25:
            matches += self.play_one_turn(turn)
            turn = (turn + 1) % num_hands

        print("---------- Game is Over")
        self.print_hands()

        self.print_loser()

    def print_loser(self):
        for hand in self.hands:
            if len(hand.cards) == 1:
                print("The loser is {0}".format(hand.name))
                break

    def print_hands(self):
        for hand in self.hands:
            print(hand)

    def remove_all_matches(self):
        count = 0
        for hand in self.hands:
            count += hand.remove_matches()
        return count
    
    def play_one_turn(self, i):
        if self.hands[i].is_empty():
            return 0
        neighbor = self.find_neighbor(i)
        picked_card = self.hands[neighbor].pop()
        self.hands[i].add(picked_card)
        print("Hand", self.hands[i].name, "picked", picked_card)
        count = self.hands[i].remove_matches()
        self.hands[i].shuffle()
        return count
    
    def find_neighbor(self, i):
        num_hands = len(self.hands)
        for next in range(1,num_hands):
            neighbor = (i + next) % num_hands
            if not self.hands[neighbor].is_empty():
                return neighbor

if __name__ == '__main__':
    game = OldMaidGame()
    game.play(["Jack", "Tom", "Ben"])