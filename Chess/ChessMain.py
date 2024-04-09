'''
Main Driver file
Responsible for handling user input and displaying the current GameState object
'''

import pygame as p
import ChessEngine

p.init()
width = height = 400
dimension = 8  # dimensions of a chess board are 8x8
sq_size = height // dimension
max_fps = 15  # for animations later on
images = {}

'''
Initialize a global dictionary of images. This will be called exactly once in the main
'''
def loadImages():
    pieces = ["wp", "wR", "wN", "wB", "wQ", "wK", "bp", "bR", "bN", "bB", "bQ", "bK"]
    for piece in pieces:
        images[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (sq_size, sq_size))
    # Note: we can access an image by saying 'images['wp']'
    
'''
The main driver for our code. This will handle user input and updating the graphics
'''
def main():
    p.init()
    screen = p.display.set_mode((width, height))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()  # only do this once, before the while loop
    running = True
    
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(max_fps)
        p.display.flip()
        
def drawGameState(screen, gs):
    """
    Draw the current game state on the screen.

    Args:
        screen: The screen object to draw on.
        gs: The game state object representing the current state of the game.
    """
    drawBoard(screen)  # draw squares on the board
    drawPieces(screen, gs.board)  # draw pieces on top of those squares
    
def drawBoard(screen):
    """
    Draw the squares on the board. The top left square is always light.

    Args:
        screen: The screen object to draw on.
    """
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(dimension):
        for c in range(dimension):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*sq_size, r*sq_size, sq_size, sq_size))

def drawPieces(screen, board):
    """
    Draw the pieces on the board using the current GameState object.

    Args:
        screen: The screen object to draw on.
        board: The board object representing the current state of the board.
    """
    for r in range(dimension):
        for c in range(dimension):
            piece = board[r][c]
            if piece != "--":  # not an empty square
                screen.blit(images[piece], p.Rect(c*sq_size, r*sq_size, sq_size, sq_size))
    

if __name__ == "__main__":
    main()