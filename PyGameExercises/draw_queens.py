import pygame

def draw_board(the_board, number=0):
    """ Draw a chess board with queens, from the_board. """

    pygame.init()
    colors = [(255,255,255), (0,0,0)] # Set up colors [white, black]

    n = len(the_board) # This is an NxN chess board.
    surface_sz = 960 # Proposed physical surface size. \

    sq_sz = surface_sz // n # sq_sz is length of a square.
    surface_sz = n * sq_sz # Adjust to exactly fit n squares.

    # Create the surface of (width, height), and its window.
    surface = pygame.display.set_mode((surface_sz, surface_sz))

    pygame.display.set_caption("Solution {0}".format(number))

    queen = pygame.image.load("PyGameExercises/queen.png")

    # Use an extra offset to centre the queen in its square.
    # If the square is too small, offset becomes negative,
    # but it will still be centered :-)
    queen_offset = (sq_sz-queen.get_width()) // 2

    while True:

        # Look for an event from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        # Draw a fresh background (a blank chess board)
        for row in range(n): # Draw each row of the board.
            c_indx = row % 2 # Change starting color on each row
            for col in range(n): # Run through cols drawing squares
                the_square = (col*sq_sz, row*sq_sz, sq_sz, sq_sz)
                surface.fill(colors[c_indx], the_square)
                # now flip the color index for the next square
                c_indx = (c_indx + 1) % 2

        # Now that squares are drawn, draw the queens.
        for (col, row) in enumerate(the_board):
            surface.blit(queen, (col * sq_sz + queen_offset, row * sq_sz + queen_offset))

        pygame.display.flip()


    pygame.quit()

if __name__ == "__main__":
    the_board = [6, 4, 2, 0, 5, 7, 1, 3]
    draw_board(the_board)
