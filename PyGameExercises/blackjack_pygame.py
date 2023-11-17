'''
Blackjack
-------------------------------------------------------------
'''

import pygame
import time
import os

class Card:
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    cards = ["na",'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    cards_dict = {'na': -1, 'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

    def __init__(self, suit, rank, img, target_posn, curr_patch_num):
        self.suit = suit
        self.card = self.cards[rank]
        self.value = self.cards_dict[self.cards[rank]]
        self.img = img
        self.init_posn = target_posn
        self.posn = target_posn
        self.card_width = 70 
        self.card_height = 103 
        self.curr_patch_num = (curr_patch_num[0] * self.card_height, curr_patch_num[1] * self.card_width)
        
    def __str__(self):
        return (self.card + " of " + self.suits[self.suit])

    def update(self):
        return
    
    def draw(self, target_surface):
        patch_rect = (self.curr_patch_num[1], self.curr_patch_num[0], self.card_width, self.card_height)
        target_surface.blit(self.img, self.posn, patch_rect)


class Deck:
    def __init__(self, playing_cards, ):
        self.cards = []
        # Create a sprite object for each card, and populate our list.
        for row in range(0, 4):
            for col in range(1, 14):
                a_card = Card(row, col, playing_cards, (0, 0), (row, col - 1)) # (row * self.card_height, (col-1) * self.card_width))
                self.cards.append(a_card)

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
        rng.shuffle(self.cards)      # Use its shuffle method

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
            
    def deal_hand(self, hand, num_cards=0):
        if not self.is_empty():
            card = self.pop()
            hand.add(card)  
            

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
    
class BlackjackGame():
    
    def __init__(self):
        
        pygame.init()
        self.surface_sz = 800 # Proposed physical surface size. \
        file_directory = os.path.dirname(os.path.realpath(__file__))
        self.playing_cards = pygame.image.load(file_directory + "/carddeck.png")
        self.card_back_red = pygame.image.load(file_directory + "/playing-card-back-red.jpg")
        self.card_back_blue = pygame.image.load(file_directory + "/playing-card-back-blue.jpg")
            
        self.deck = Deck(self.playing_cards)
        self.deck.shuffle()
        
        # Make a hand for each player
        self.hands = []
        for name in ["Player", "Dealer"]:
            self.hands.append(Hand(name))
            
        self.player_score = 0
        self.dealer_score = 0
        
        # Create a font for rendering text
        self.my_font = pygame.font.SysFont("Courier", 22)
        self.my_font2 = pygame.font.SysFont("Courier", 32)
        self.my_font_label = pygame.font.SysFont("Courier", 24)
        # Make a new surface with an image of the text
        self.update_instruction("Press SPACE to deal the first card...")
        self.the_text = self.my_font.render("Press SPACE to deal the first card...", True, (0,0,0))
        self.player_text = self.my_font2.render("PLAYER", True, (0,0,255))
        self.dealer_text = self.my_font2.render("DEALER", True, (0,0,255))
        self.pl_score = self.my_font.render(f"Player score: {self.player_score}", True, (0,0,0))
        self.de_score = self.my_font.render(f"Dealer score: {self.dealer_score}", True, (0,0,0))
        self.result_text = self.my_font2.render("", True, (255,0,0))
        
        # step between cards on table
        self.x_step = self.surface_sz / 6
        self.y_step = self.surface_sz / 3
            
    def deal(self, num_cards=0):
        self.deck.deal(self.hands, num_cards)
        
    def deal_hand(self, hand_index=0, num_cards=0):
        self.deck.deal_hand(self.hands[hand_index], num_cards)
        
    def update_scores(self, both_scores=True):
        for (i, hand) in enumerate(self.hands):
            for (c, card) in enumerate(hand.cards):
                card.posn = (i * self.y_step + self.y_step, c * self.x_step + self.x_step)
                if hand.name == "Player":
                    self.player_score += card.value
                    self.pl_score = self.my_font.render(f"Player score: {self.player_score}", True, (0,0,0))
                else:
                    if both_scores:
                        self.dealer_score += card.value
                        self.de_score = self.my_font.render(f"Dealer score: {self.dealer_score}", True, (0,0,0))
                    else:
                        # Do not update for dealer as card is hidden
                        pass
                    
    def update_instruction(self, instr=""):
        self.the_text = self.my_font.render(instr, True, (0,0,0))
        
    def update_result(self, result=""):
        self.result_text = self.my_font2.render(result, True, (255,0,0))

    def play(self):
        """ Draw a poker table and play blackjack"""

        my_clock = pygame.time.Clock()

        # Create the surface of (width, height), and its window.
        surface = pygame.display.set_mode((self.surface_sz, self.surface_sz))

        pygame.display.set_caption("Blackjack")

        a_card_red = Card(0, 0, self.card_back_red, (0, 0), (0, 0))
        a_card_blue = Card(0, 0, self.card_back_blue, (0, 0), (0, 0))

        # Deal the cards
        self.deal(2)
                    
        round_count = 0
        game_over = False
        dealer_playing = False

        while True:
            # Look for an event from keyboard, mouse, etc.
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                break

            if ev.type == pygame.KEYDOWN and not game_over:
                key = ev.dict["key"]
                # reset scores
                self.player_score = 0
                self.dealer_score = 0
                
                # user is playing
                if not dealer_playing:
                    # User presses Space
                    if key == pygame.K_SPACE: 
                        if round_count == 0:
                            
                            self.update_scores()
                                    
                            self.update_instruction("Press SPACE to get another card...")
                            # Deal the card for the player
                            self.deal_hand(0, 1)
                            # If dealt an Ace, adjust score for each existing Ace in hand
                            if self.player_score > 21:
                                for card in self.hands[0].cards:
                                    if card.value == 11:
                                        card.value = 1
                                    
                            round_count += 1
                        elif round_count == 1:
                            
                            self.update_scores()
                                        
                            self.update_instruction("Press SPACE to get another card...")
                            # Deal the card for the dealer
                            self.deal_hand(1, 1)
                            
                            # If dealt an Ace, adjust score for each existing Ace in hand
                            if self.dealer_score > 21:
                                for card in self.hands[1].cards:
                                    if card.value == 11:
                                        card.value = 1
                            
                            round_count += 1
                        elif round_count == 2:
                            
                            self.update_scores(False)
                            
                            a_card_blue.posn = (self.y_step + self.y_step, self.x_step + self.x_step)
                                        
                            self.update_instruction("Press H to hit or S to Stand...")
                            
                            round_count += 1
                    # User presses H
                    if key == pygame.K_h: 
                        if round_count == 3:
                            # Deal the card for the player
                            self.deal_hand(0, 1)
                            
                            # If dealt an Ace, adjust score for each existing Ace in hand
                            if self.player_score > 21:
                                for card in self.hands[0].cards:
                                    if card.value == 11:
                                        card.value = 1
                            
                            self.update_scores(False)
                            
                            # check score
                            if self.player_score == 21:
                                self.update_instruction("")
                                self.update_result("PLAYER HAS A BLACKJACK, PLAYER WINS!!!")
                                game_over = True
                            elif self.player_score > 21:
                                self.update_instruction("")
                                self.update_result("PLAYER BUSTED!!! GAME OVER!!!")
                                game_over = True

                    # User presses S
                    if key == pygame.K_s: 
                        if round_count == 3:
                            time.sleep(1)   
                            
                            self.update_scores()
                                        
                            a_card_blue.posn = a_card_blue.init_posn
                            
                            self.update_instruction("")
                            
                            # check score
                            if self.player_score == 21:
                                self.update_result("PLAYER HAS A BLACKJACK, PLAYER WINS!!!")
                                game_over = True
                            elif self.player_score > 21:
                                self.update_result("PLAYER BUSTED!!! GAME OVER!!!")
                                game_over = True
                            else:
                                if self.dealer_score == 21:
                                    self.update_result("DEALER HAS A BLACKJACK, DEALER WINS!!!")
                                    game_over = True
                                elif self.dealer_score > self.player_score:
                                    self.update_result("DEALER WINS!!! GAME OVER!!!")
                                    game_over = True
                                else:
                                    self.update_instruction("Press D to let the Dealer play...")
                                    dealer_playing = True
                # dealer is playing
                else:
                    # User presses D and let the dealer play
                    if key == pygame.K_d:
                        time.sleep(1) 
                        
                        # Deal the card for the dealer
                        self.deal_hand(1, 1)
                        
                        # If dealt an Ace, adjust score for each existing Ace in hand
                        if self.dealer_score > 21:
                            for card in self.hands[1].cards:
                                if card.value == 11:
                                    card.value = 1
                                    
                        self.update_scores()
                        
                        self.update_instruction("")
                                        
                        if self.dealer_score == 21:
                            self.update_result("DEALER HAS A BLACKJACK, DEALER WINS!!!")
                            game_over = True
                        elif self.dealer_score > 21:
                            self.update_result("DEALER BUSTED!!! PLAYER WINS!!!")
                            game_over = True
                        elif self.dealer_score > self.player_score:
                            self.update_result("DEALER WINS!!! GAME OVER!!!")
                            game_over = True
                        else:
                            self.update_instruction("Press D to let the Dealer play...")
            
            # Draw a fresh background (a green poker cloth)
            surface.fill((85, 170, 85))

            # Ask cards to draw itself.
            for card in self.deck.cards:
                card.draw(surface)
            
            # Ask cards in hands to draw itself.
            for hand in self.hands:
                for card in hand.cards:
                    card.draw(surface)
            
            # Ask back cards to draw itself
            a_card_blue.draw(surface)
            a_card_red.draw(surface)
            
            # Copy the instructions to the main surface
            surface.blit(self.the_text, (self.surface_sz / 4, 10))
            
            surface.blit(self.player_text, (self.y_step - 30, self.x_step - 40) )
            surface.blit(self.dealer_text, (self.y_step * 2 - 30, self.x_step - 40) )
            
            # Copy the score to the main surface
            surface.blit(self.pl_score, (self.surface_sz - 220, self.surface_sz - 70))
            surface.blit(self.de_score, (self.surface_sz - 220, self.surface_sz - 35))
            
            # Copy the result to the main surface
            surface.blit(self.result_text, (20, self.surface_sz - 120))

            pygame.display.flip()
            my_clock.tick(60)
        
        pygame.quit()


if __name__ == '__main__':
    game = BlackjackGame()
    game.play()
