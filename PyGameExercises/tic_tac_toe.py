'''
Tic Tac Toe
-------------------------------------------------------------
'''


import random
import pygame


class TicTacToe:

    def __init__(self, sq_sz=0, x_sym=None, o_sym=None, sym_offset=0):
        self.board = []
        self.sq_sz = sq_sz
        self.x_sym = x_sym
        self.o_sym = o_sym
        self.sym_offset = sym_offset

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player
        
    def is_spot_free(self, row, col):
        return self.board[row][col] == "-"

    def has_player_won(self, player):
        n = len(self.board)
        board_values = set()

        # check rows
        for i in range(n):
            for j in range(n):
                board_values.add(self.board[i][j])

            if board_values == {player}:
                return True
            else:
                board_values.clear()

        # check cols
        for i in range(n):
            for j in range(n):
                board_values.add(self.board[j][i])

            if board_values == {player}:
                return True
            else:
                board_values.clear()

        # check diagonals
        for i in range(n):
            board_values.add(self.board[i][i])
        if board_values == {player}:
            return True
        else:
            board_values.clear()
        
        board_values.add(self.board[0][2])
        board_values.add(self.board[1][1])
        board_values.add(self.board[2][0])
        if board_values == {player}:
            return True
        else:
            return False

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=' ')
            print()

    def start(self):
        self.create_board()
        player = 'X' if self.get_random_first_player() == 1 else 'O'
        game_over = False

        while not game_over:
            try:
                self.show_board()
                print(f'\nPlayer {player} turn')

                row, col = list(
                    map(int, input(
                        'Enter row & column numbers to fix spot: ').split()))
                print()
                
                if col < 1 or row < 1:
                    raise ValueError("The values of row and column can only be 1, 2 or 3!")

                if col is None:
                    raise ValueError(
                        'not enough values to unpack (expected 2, got 1)')

                if not self.is_spot_free(row - 1, col - 1):
                        raise ValueError(f"{row} {col} has been taken already!")

                self.fix_spot(row - 1, col - 1, player)

                game_over = self.has_player_won(player)
                if game_over:
                    print(f'Player {player} wins the game!')
                    continue

                game_over = self.is_board_filled()
                if game_over:
                    print('Match Draw!')
                    continue

                player = self.swap_player_turn(player)

            except ValueError as err:
                print(err)

        print()
        self.show_board()
       
    def draw(self, row, col, target_surface):
        if len(self.board) > 0:
            if self.board[row][col] == 'X':
                target_surface.blit(self.x_sym, (row * self.sq_sz + self.sym_offset, col * self.sq_sz + self.sym_offset))
            elif self.board[row][col] == 'O':
                target_surface.blit(self.o_sym, (row * self.sq_sz + self.sym_offset, col * self.sq_sz + self.sym_offset))


def draw_board():
    """ Draw a tic tac toe board """

    pygame.init()
    colors = [(255,255,255), (0,0,0)] # Set up colors [white, black]

    n = 3 # This is an NxN board.
    surface_sz = 960 # Proposed physical surface size. \

    sq_sz = surface_sz // n # sq_sz is length of a square.
    surface_sz = n * sq_sz # Adjust to exactly fit n squares.

    # Create the surface of (width, height), and its window.
    surface = pygame.display.set_mode((surface_sz, surface_sz))

    pygame.display.set_caption("Tic Tac Toe")

    x_sym = pygame.image.load("PyGameExercises/x.png")
    
    o_sym = pygame.image.load("PyGameExercises/o.png")

    # Use an extra offset to centre the symbol in its square.
    # If the square is too small, offset becomes negative,
    # but it will still be centered :-)
    x_sym_offset = (sq_sz-x_sym.get_width()) // 2
    o_sym_offset = (sq_sz-o_sym.get_width()) // 2
    
    tic_tac_toe = TicTacToe(sq_sz, x_sym, o_sym, x_sym_offset)
    tic_tac_toe.create_board()
    
    player = 'X' if tic_tac_toe.get_random_first_player() == 1 else 'O'
    game_over = False

    while True:

        # Look for an event from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        
        if ev.type == pygame.MOUSEBUTTONDOWN: # Mouse gone down?
            posn_of_click = ev.dict["pos"] # Get the coordinates.
            (x, y) = posn_of_click
            row = x // sq_sz + 1
            col = y // sq_sz + 1
            if tic_tac_toe.is_spot_free(row - 1, col - 1):
                tic_tac_toe.fix_spot(row - 1, col - 1, player)
                    
                game_over = tic_tac_toe.has_player_won(player)
                if game_over:
                    print(f'Player {player} wins the game!')
                    break

                game_over = tic_tac_toe.is_board_filled()
                if game_over:
                    print('Match Draw!')
                    break
                
                player = tic_tac_toe.swap_player_turn(player)

        # Draw a fresh background (a blank board)
        for row in range(n): # Draw each row of the board.
            c_indx = row % 2 # Change starting color on each row
            for col in range(n): # Run through cols drawing squares
                the_square = (col*sq_sz, row*sq_sz, sq_sz, sq_sz)
                surface.fill(colors[c_indx], the_square)
                # now flip the color index for the next square
                c_indx = (c_indx + 1) % 2

        # Ask every symbol to draw itself.
        for row in range(3):
            for col in range(3):
                tic_tac_toe.draw(row, col, surface)

        pygame.display.flip()


    pygame.quit()

if __name__ == '__main__':
    tic_tac_toe = TicTacToe()
    draw_board()
#   tic_tac_toe.start()
  