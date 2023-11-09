import pygame
import random

class CardSprite:

    def __init__(self, img, target_posn, curr_patch_num):
        self.img = img
        self.init_posn = target_posn
        self.posn = target_posn
        self.curr_patch_num = curr_patch_num
        self.card_width = 34.61
        self.card_height = 53

    def update(self):
        return
    
    def draw(self, target_surface):
        """each card has width = 34.61 and height = 53"""
        patch_rect = (self.curr_patch_num[1], self.curr_patch_num[0], self.card_width, self.card_height)
        target_surface.blit(self.img, self.posn, patch_rect)

    def handle_click(self, index):
        self.posn = (50 * index + 50, self.init_posn[1] - 200)

    def reset_pos(self):
        self.posn = self.init_posn
    
    
def draw_playing_cards():
    """ Draw a poker table, shuffle the cards and draw the top 5"""

    pygame.init()

    my_clock = pygame.time.Clock()

    surface_sz = 800 # Proposed physical surface size. \

    # Create the surface of (width, height), and its window.
    surface = pygame.display.set_mode((surface_sz, surface_sz))

    pygame.display.set_caption("Playing cards")

    playing_cards = pygame.image.load("PyGameExercises/carddeck.png")

    all_cards = []

    # Create a sprite object for each card, and populate our list.
    for row in range(0, 4):
        for col in range(0, 13):
            a_card = CardSprite(playing_cards, (0, surface_sz - 55), (row*53, col*34.61))
            all_cards.append(a_card)

    random.shuffle(all_cards)
    top_five = []
    for (i, card) in enumerate(all_cards):
        if i < 5:
            top_five.append(card)

    while True:
        # Look for an event from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        if ev.type == pygame.KEYDOWN:
            key = ev.dict["key"]
            if key == pygame.K_SPACE: 
                for card in top_five:
                    card.reset_pos()
                # choose 5 new cards
                top_five.clear()
                random.shuffle(all_cards)
                for (i, card) in enumerate(all_cards):
                    if i < 5:
                        top_five.append(card)
                # show them
                for (i, card) in enumerate(top_five):
                    card.handle_click(i)
        
        # Ask every sprite to update itself.
        for card in all_cards:
            card.update()

        # Draw a fresh background (a green poker cloth)
        surface.fill((0,255, 0))

        # Ask first 5 sprites to draw itself.
        # for i in range(0, 5):
            # s = random.choice(all_cards)
        for card in all_cards:
            card.draw(surface)

        pygame.display.flip()
        my_clock.tick(60)
    
    pygame.quit()


if __name__ == "__main__":
    draw_playing_cards()