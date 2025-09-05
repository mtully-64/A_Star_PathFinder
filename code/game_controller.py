import pygame
from grid_manager import GridManager
from astar_algorithm import astar_algorithm
from constants import ROWS

class GameController:
    def __init__(self, win, width):
        self.win = win
        self.width = width
        self.grid_manager = GridManager(ROWS, width)
        self.start = None
        self.end = None
        self.running = True

    def handle_mouse_click(self, pos, button):
        """Handle mouse click events"""
        row, col = self.grid_manager.get_clicked_position(pos)
        node = self.grid_manager.get_node(row, col)
        
        if not node:
            return

        if button == 1:  # Left click
            if not self.start and node != self.end:
                self.start = node
                self.start.make_start()
            elif not self.end and node != self.start:
                self.end = node
                self.end.make_end()
            elif node != self.end and node != self.start:
                node.make_barrier()
                
        elif button == 3:  # Right click
            node.reset()
            if node == self.start:
                self.start = None
            elif node == self.end:
                self.end = None

    def handle_keypress(self, key):
        """Handle keyboard events"""
        if key == pygame.K_SPACE and self.start and self.end:
            self.run_algorithm()
        elif key == pygame.K_c:
            self.clear_grid()

    def run_algorithm(self):
        """Run the A* pathfinding algorithm"""
        self.grid_manager.update_all_neighbours()
        astar_algorithm(
            lambda: self.grid_manager.draw(self.win),
            self.grid_manager.grid,
            self.start,
            self.end
        )

    def clear_grid(self):
        """Clear the grid and reset start/end points"""
        self.start = None
        self.end = None
        self.grid_manager.reset_grid()

    def run(self):
        """Main game loop"""
        while self.running:
            self.grid_manager.draw(self.win)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if pygame.mouse.get_pressed()[0]:  # Left click held
                    pos = pygame.mouse.get_pos()
                    self.handle_mouse_click(pos, 1)
                elif pygame.mouse.get_pressed()[2]:  # Right click held
                    pos = pygame.mouse.get_pos()
                    self.handle_mouse_click(pos, 3)

                if event.type == pygame.KEYDOWN:
                    self.handle_keypress(event.key)

        pygame.quit()