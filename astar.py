import pygame
import math
from queue import PriorityQueue

# Defining the width and height of my window for the game
WIDTH = 800

# Defining the window size of the game
WIN = pygame.display.set_mode((WIDTH, WIDTH))

# Setting title for the window
pygame.display.set_caption("A* Path Finding Algorithm")

# Defining colour RGB values
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (0, 0, 255)
BLACK = (255, 255, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# Now I will define a class to for the visualisation of a node for the game
class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.colour = WHITE 
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col
    
    def is_closed(self):
        return self.colour == RED
    
    def is_open(self):
        return self.colour == GREEN
    
    def is_barrier(self):
        return self.colour == BLACK
    
    def is_start(self):
        return self.colour == ORANGE
    
    def is_end(self):
        return self.colour == TURQUOISE
    
    def reset(self):
        self.colour == WHITE
    
    def make_closed(self):
        self.colour = RED
    
    def make_open(self):
        self.colour = GREEN
    
    def make_barrier(self):
        self.colour = BLACK
    
    def make_end(self):
        self.colour = TURQUOISE

    def make_path(self):
        self.colour = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.colour, ())