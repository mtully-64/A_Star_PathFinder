import pygame
from game_controller import GameController
from constants import WIDTH

def main():
    """Main application"""
    pygame.init()
    
    # Create game window
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("A* Path Finding Algorithm")
    
    # Create and run game controller
    game = GameController(win, WIDTH)
    game.run()

if __name__ == "__main__":
    main()